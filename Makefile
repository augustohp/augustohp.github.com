RUBY_VERSION=3.3
DOCKERFILE_PATH=usr/Dockerfile

.PHONY: serve
serve:
	docker compose up --build

.PHONY: shell
shell:
	docker compose run --rm jekyll bash

.PHONY: post
post:
	@./bin/new-post.sh ${TITLE}

.PHONY: links
links:
	lychee --config .lychee.toml --output report-broken-links.txt . 

clean:
	rm -rf _site

.PHONY: upgrade-ruby
upgrade-ruby:
	sed -E -i "s#^(ruby '~> )([0-9\.]*)#\1${RUBY_VERSION}#" Gemfile
	sed -E -i 's/^(FROM ruby:)([0-9\.]*)/\1${RUBY_VERSION}/' "${DOCKERFILE_PATH}"
	docker run --rm -v $(PWD):/app -w /app ruby:${RUBY_VERSION} bundle update