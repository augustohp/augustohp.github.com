server:
	jekyll serve --watch --detach --future --quiet

post:
	@./bin/new-post.sh ${TITLE}

.PHONY: server post
