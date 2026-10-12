#!/usr/bin/env python3
"""Integration regression: real Jekyll HTML, real Lychee spans, workflow output."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import textwrap
from threading import Thread


ROOT = Path(__file__).resolve().parent.parent


class Missing(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_error(404)

    def log_message(self, *args):
        pass


with tempfile.TemporaryDirectory(prefix="test-link-report-") as directory:
    work = Path(directory)
    posts = work / "_posts"
    posts.mkdir()
    shutil.copy(ROOT / "_config.yml", work)
    env = {**os.environ, "BUNDLE_GEMFILE": str(ROOT / "Gemfile")}
    report = {"error_map": {}, "timeout_map": {}}
    examples = [
        ("2011-09-06-Singleton-#not.md", "https://www.oracle.com/java/technologies/front-controller.html",
         "/php,%20design%20patterns/2011/09/06/Singleton-not.html#onde-o-controle-de-natalidade-falha"),
        ("2015-04-29-porque-vim.md", "https://wordpress.com/",
         "/desenvolvimento/2015/04/30/porque-vim.html#comendo-boa-comida"),
        ("2011-03-15-event-emitters.md", "https://www.npmjs.com/",
         "/nodejs/2011/03/15/event-emitters.html#page-title"),
    ]
    for filename, url, _ in examples:
        shutil.copy(ROOT / "_posts" / filename, posts)
        report["error_map"][f"./_posts/{filename}"] = [{"url": url, "status": {"code": 403, "text": "403"}}]

    server = ThreadingHTTPServer(("127.0.0.1", 0), Missing)
    Thread(target=server.serve_forever, daemon=True).start()
    broken = f"http://127.0.0.1:{server.server_port}/missing?a=1&b=2"
    dated = posts / "2001-01-02-wrong-filename.md"
    dated.write_text(f"""---
layout: post
title: Fixture
date: 2014-06-07
categories: [First, Second]
---
Intro [first]({broken}).

## Repetida

[reference][same]

## Repetida

<a href="{broken.replace('&', '&amp;')}">escaped &amp; repeated</a>

[same]: {broken}
""")
    custom = posts / "2002-02-03-custom.md"
    custom.write_text(f"""---
layout: post
title: Custom
permalink: /custom/space here/%25literal/
---
## Ação & café

[custom]({broken})
""")
    try:
        result = subprocess.run([
            "lychee", "--cache=false", "--max-retries", "0", "--format", "json",
            "--output", str(work / "lychee.json"), str(dated), str(custom)
        ], cwd=work, capture_output=True, text=True)
        assert result.returncode == 2, result.stderr
    finally:
        server.shutdown()
        server.server_close()
    lychee = json.loads((work / "lychee.json").read_text())
    assert {link["url"] for links in lychee["error_map"].values() for link in links} == {broken}
    report["error_map"].update(lychee["error_map"])
    spans = [link["span"] for links in lychee["error_map"].values() for link in links]
    assert spans and all(isinstance(span["line"], int) and isinstance(span["column"], int) for span in spans)
    report_path = work / "report-broken-links.json"
    report_path.write_text(json.dumps(report))
    index_path = work / "link-report-sources.json"
    subprocess.run(["python3", str(ROOT / "bin/link-report-sources.py"), str(report_path), str(index_path)],
                   cwd=work, env=env, check=True, capture_output=True)
    index = json.loads(index_path.read_text())
    origin = "https://blog.augustopascutti.com"
    for filename, url, expected in examples:
        assert index[str(posts / filename)]["links"][url] == [origin + expected]
    dated_url = origin + "/first/second/2014/06/07/wrong-filename.html"
    assert index[str(dated)]["links"][broken] == [
        dated_url + "#page-title", dated_url + "#repetida", dated_url + "#repetida-1"
    ]
    assert index[str(custom)]["links"][broken] == [
        origin + "/custom/space%20here/%25literal/#a%C3%A7%C3%A3o--caf%C3%A9"
    ]

    # Execute the actual workflow script locally; never contact the GitHub API.
    workflow = (ROOT / ".github/workflows/link.yaml").read_text()
    script = textwrap.dedent(workflow.split("          script: |\n", 1)[1])
    runner = work / "workflow.cjs"
    runner.write_text("""
const assert = require('node:assert/strict');
const fs = require('node:fs');
const run = new (Object.getPrototypeOf(async function(){}).constructor)('require', 'core', 'github', 'context', SCRIPT);
const context = {serverUrl: 'https://github.com', repo: {owner: 'augustohp', repo: 'augustohp.github.com'}, sha: 'test', runId: 123};
(async () => {
  for (const create of ['false', 'true']) {
    process.env.CREATE_ISSUE = create;
    let updated;
    const github = {paginate: async () => [{number: 99, title: '🤖 Broken Links Report'}, {number: 58, title: '🤖 Broken Links Report'}],
      rest: {issues: {listForRepo: {}, update: async args => {updated = args;}, create: async () => {throw Error('Unexpected create');}}}};
    if (create === 'false') github.paginate = async () => {throw Error('create_issue=false accessed GitHub');};
    const core = {summary: {addRaw(body) {this.body = body; return this;}, async write() {}}, setFailed() {}, warning() {}};
    await run(require, core, github, context);
    const body = fs.readFileSync('report-broken-links.md', 'utf8');
    assert.equal(body, core.summary.body);
    assert(body.includes('#page-title>'));
    assert(body.includes('#repetida-1>'));
    assert(!body.includes('(source: _posts/'));
    if (create === 'true') {assert.equal(updated.issue_number, 58); assert.equal(updated.body, body);}
  }
  // Rendering unavailable: preserve reporting, with escaped repository URLs.
  fs.unlinkSync('link-report-sources.json');
  process.env.CREATE_ISSUE = 'false';
  const core = {summary: {addRaw() {return this;}, async write() {}}, setFailed() {}, warning() {}};
  await run(require, core, {}, context);
  const fallback = fs.readFileSync('report-broken-links.md', 'utf8');
  assert(fallback.includes('/blob/test/_posts/2011-09-06-Singleton-%23not.md>'));
  assert(fallback.includes('#L'));

  const cases = [
    {errors: [['https://wordpress.com/', 403], ['https://www.npmjs.com/', 403]], failed: false, writes: false, verified: 2},
    {errors: [], exit: '0', failed: false, writes: false},
    {errors: [['https://wordpress.com/', 404]], failed: true, writes: true},
    {errors: [['https://www.npmjs.com/', 500]], failed: true, writes: true},
    {errors: [['https://wordpress.com/missing', 403]], failed: true, writes: true},
    {errors: [['https://example.com/', 403]], failed: true, writes: true},
    {errors: [['https://wordpress.com/', 403], ['https://example.com/', 404]], failed: true, writes: true},
    {errors: [], timeout: 'https://www.npmjs.com/', failed: true, writes: true},
    {errors: [['https://www.npmjs.com/', 403]], exit: '1', failed: true, writes: false},
    {errors: [], failed: true, writes: false},
    {errors: [['https://example.com/', 429]], failed: false, writes: true},
  ];
  for (const test of cases) {
    fs.writeFileSync('report-broken-links.json', JSON.stringify({
      error_map: {'test.md': test.errors.map(([url, code]) => ({url, status: {code, text: String(code)}}))},
      timeout_map: test.timeout ? {'test.md': [{url: test.timeout, status: {text: 'Timeout'}}]} : {},
    }));
    process.env.CREATE_ISSUE = 'true';
    process.env.LYCHEE_EXIT_CODE = test.exit ?? '2';
    let failed = false;
    let written = false;
    const core = {summary: {addRaw() {return this;}, async write() {}}, setFailed() {failed = true;}, warning() {}};
    const github = {paginate: async () => {
      assert(test.writes, 'Known verified 403s must not access the issue API');
      return [{number: 58, title: '🤖 Broken Links Report'}];
    }, rest: {issues: {listForRepo: {}, update: async () => {written = true;}}}};
    await run(require, core, github, context);
    assert.equal(failed, test.failed, JSON.stringify(test));
    assert.equal(written, test.writes, JSON.stringify(test));
    if (test.verified) assert(fs.readFileSync('report-broken-links.md', 'utf8').includes(`Manually verified links / known 403 blocking (${test.verified})`));
  }
})().catch(error => {console.error(error); process.exit(1);});
""".replace("SCRIPT", json.dumps(script)))
    subprocess.run(["node", str(runner)], cwd=work,
                   env={**env, "RUNNER_TEMP": str(work), "LYCHEE_EXIT_CODE": "2"}, check=True)
    print("PASS: published source anchors; real Lychee spans; no-write mode; issue selection/fallback; exact verified 403s; changed status, unrelated URL, timeout and infrastructure failures")
