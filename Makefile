.title:
	@echo "Augusto Pascutti - Blogging Plataform"

server:
	jekyll serve --watch --detach --future --quiet

post: .title
	@echo "Creating post: ${TITLE}"
	touch _posts/`date "+%Y-%m-%d-"`${TITLE}
	@git status --short

.PHONY: server post
