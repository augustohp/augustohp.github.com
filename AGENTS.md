# Repository guidance

## Broken-link-fixer role

For link repairs, load `.agents/skills/fixing-broken-links/SKILL.md` and follow
the `broken-link-fixer` role defined there. It can run in the current thread;
no separate agent or thread is required. When delegating an explicitly requested
repair, supply the report/run URL and the owned source files, and ask the worker
to read that skill before editing.

Preserve historical prose, link labels, post dates, and routes. Repair the
destination, not the article. Do not weaken the link checker to hide failures.

## Validation

- Link checks: `lychee --config .lychee.toml --cache=false --output /tmp/blog-links.md <changed-posts>`.
- Build: `bundle exec jekyll build --destination /tmp/blog-site`.
- If Ruby/Bundler are absent from PATH, use the mise toolchain installed by
  `.agents/setup`, with versions from `Gemfile.lock`; see `README.md`.
- Keep temporary probes and reports outside the source tree. Do not publish
  agent instructions or checker output with the blog.
