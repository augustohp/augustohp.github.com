.title:
	@echo "Augusto Pascutti - Blogging Plataform"

server:
	jekyll serve --watch --detach --future --quiet

post: .title
	@./bin/new-post.sh ${TITLE}

.PHONY: server post
