---
name: fixing-broken-links
description: Repairs historical blog links using Augusto's canonical-URL and Wayback approach. Use as the broken-link-fixer role for link-health reports and dead post references.
---

# Broken-link-fixer

Restore access to the referenced content without rewriting historical posts.

## Established approach

Read these commits when choosing replacements:

- `75401e3c3bc3a785b5c31f1cc0bc0ba7c0a30fae`: replace dead pages with dated
  Wayback snapshots, migrated project sites, and commit-pinned source files.
- `fdf1337e8aedfa55156b6d8fe17776c592d70e6c`: keep link text and prose, prefer
  HTTPS, and use reference-style links for unwieldy archive URLs.
- `8ddbfa352524a504dbf8f151d64b7ff8d7b097a4`: replace a broken short URL with
  the original commit's durable repository URL.
- Augusto's Wayback lookup method is in
  `https://gist.github.com/augustohp/fdac0243bbd14ca3d1dff09725726a10`.
  Fetch and inspect it, rather than executing downloaded code blindly.

## Repair procedure

1. Inspect the latest exact-title `🤖 Broken Links Report` body, comments,
   timestamps, and linked workflow run. Deduplicate URLs for research, but
   track every source occurrence. Old observations are not current failures.
2. Read the surrounding article and reproduce the reported URL failure with
   the repository's Lychee configuration and cache disabled. Use bounded GETs
   with redirects to inspect the actual response and final destination.
   A 200 challenge page is not working content; a 403/429/anti-bot response is
   not proof the content disappeared. Report uncertain links separately.
3. Prefer the exact content on its current canonical HTTPS URL. For manuals,
   an upstream-linked mirror of the same section is suitable; verify fragments.
   A project or film link may use a verified maintainer/distributor page for
   the same subject. Do not substitute a generic homepage for a lost article.
4. If the content is gone, query Wayback using the original URL and a timestamp
   appropriate to the post, following Augusto's gist:

   ```sh
   curl --fail --silent --show-error --location --max-time 30 --get \
     https://archive.org/wayback/available \
     --data-urlencode "url=$url" --data-urlencode "timestamp=$timestamp" \
     | jq '.archived_snapshots.closest'
   ```

   An empty result is not a replacement. Inspect the returned snapshot's
   content and redirects before editing. Do not invent snapshot dates or call
   an archived URL verified merely because Lychee excludes archive.org.
5. Change only the destination/reference definition. Preserve prose, labels,
   frontmatter, routes, and unrelated typos. Do not add exclusions or accept
   error statuses just to make a report green.
6. Re-run the same cache-free check on changed posts, validate new fragments,
   and build Jekyll. Inspect rendered hrefs and unchanged labels. Report the
   before/after failures honestly, including remaining blocked URLs.

## Reporting and delivery boundaries

The active Link Health workflow runs weekly on Monday at 10:00 UTC (07:00 in
America/Fortaleza). Verify its current state and recent runs before assuming
it ran. Dispatching it with `create_issue=true` writes shared GitHub state and
requires explicit authorization. Do not trigger deployments while fixing links.

The workflow updates the lowest-numbered open exact-title issue and replaces
its body; preserve investigation notes in comments when authorized. Healthy
runs do not update or close the issue. Do not close it on a local green check.

Return replacements with evidence, validation commands/results, unresolved
URLs, and the actual delivery state. Pushing, opening a PR, merging, and
deploying are separate shared-state actions; obtain the relevant authorization.
