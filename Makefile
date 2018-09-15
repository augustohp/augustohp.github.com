.PHONY: serve
serve:
	bundle exec jekyll serve

.PHONY: post
post:
	@./bin/new-post.sh ${TITLE}
