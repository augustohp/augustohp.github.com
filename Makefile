.title:
	@echo "Augusto Pascutti - Blogging Plataform"

post: .title
	@echo "Creating post: ${TITLE}"
	touch _posts/`date "+%Y-%m-%d-"`${TITLE}
	@git status --short
