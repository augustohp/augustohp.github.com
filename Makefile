.PHONY: serve
serve:
	docker compose up

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