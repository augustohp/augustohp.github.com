#!/usr/bin/env python3
"""Index report URLs against Jekyll's published HTML, without changing posts."""

import json
import os
from html.parser import HTMLParser
from pathlib import Path
import subprocess
import sys
import tempfile
from urllib.parse import quote, urljoin


class Sections(HTMLParser):
    def __init__(self, html, page_url):
        super().__init__(convert_charrefs=True)
        self.page_url = page_url
        self.section = None
        self.links = {}
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("h1", "h2", "h3", "h4", "h5", "h6") and attrs.get("id"):
            self.section = attrs["id"]
        if tag in ("a", "img") and attrs.get("href" if tag == "a" else "src"):
            href = attrs["href" if tag == "a" else "src"]
            # Match Lychee's URL serialization, including HTML entities and spaces.
            href = quote(urljoin(self.page_url, href), safe=":/?#[]@!$&'()*+,;=%")
            location = self.page_url
            if self.section:
                location += "#" + quote(self.section, safe="")
            locations = self.links.setdefault(href, [])
            if location not in locations:
                locations.append(location)


def build_sources(report_path, output_path):
    report = json.loads(Path(report_path).read_text())
    sources = {
        str(Path(source).resolve())
        for key in ("error_map", "timeout_map")
        for source in report.get(key, {})
    }
    # Let the exact locked Jekyll/Pages stack own dates, categories, permalinks,
    # exclusions and Liquid. Keep the build outside Lychee's input directory.
    with tempfile.TemporaryDirectory(prefix="link-report-") as temporary:
        manifest = Path(temporary) / "sources.json"
        subprocess.run([
            "bundle", "exec", "ruby", "-e", """
require 'jekyll'
require 'json'
Jekyll::PluginManager.require_from_bundler
site = Jekyll::Site.new(Jekyll.configuration(
  'destination' => ARGV[0], 'safe' => true, 'quiet' => true
))
site.process
documents = site.pages + site.collections.values.flat_map(&:docs)
manifest = documents.select { |doc| doc.output && doc.write? }.map do |doc|
  url = Liquid::Template.parse('{{ path | absolute_url }}').render!(
    site.site_payload.merge('path' => doc.url), registers: { site: site }
  )
  { source: File.expand_path(doc.path, site.source), url: url, html: doc.output }
end
File.write(ARGV[1], JSON.generate(manifest))
""", str(Path(temporary) / "site"), str(manifest)
        ], check=True, env={**os.environ, "JEKYLL_ENV": "production"})
        pages = json.loads(manifest.read_text())

    index = {}
    for page in pages:
        if page["source"] not in sources:
            continue
        page_url = quote(page["url"], safe=":/?#[]@!$&'()*+,;=%")
        index[page["source"]] = {
            "url": page_url,
            "links": Sections(page["html"], page_url).links,
        }
    Path(output_path).write_text(json.dumps(index, ensure_ascii=False))


if __name__ == "__main__":
    build_sources(*sys.argv[1:])
