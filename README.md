# Meu "Blog"

Alguns textos que deveriam ter ido pro limbo, mas que de alguma forma vieram parar aqui.
Pelo menos estão decentemente versionados.

## Como ele funciona?

* [GitHub Pages](https://pages.github.com) para transformar este repositório num site.
* [SASS](https://sass-lang.com/) pra tentar manter o CSS são.
* [Git](https://git-scm.com) para versionar os textos.
* [Markdown](https://daringfireball.net/projects/markdown/) para manter os textos legíveis.
* [Disqs](https://disqus.com/) para os comentários.

Tenho usado [Git](https://git-scm.com) por tempo o suficiente pra querer 
tudo versionado nele, porquê não o blog?

Escrever (e ler HTML) não é lá muito confortável, estive acostumado a escrever
em [Markdown](https://daringfireball.net/projects/markdown/) durante tanto tempo
que o faço sem nem perceber.

Estou bastante convencido do workflow que tenho pro *blog*, apesar de não usar
ele tanto assim é o **workflow do meu dia a dia**. Difícil que qualquer gerenciador
de conteúdo, mesmo que baseado nas mesmas tecnologias, seja melhor do que esse
conjunto de ferramentas pra mim.

## Desenvolvimento em orbs do Amp

O Amp executa `.agents/setup` ao preparar um orb novo e guarda o ambiente em um
snapshot reutilizável. O script instala Ruby e Bundler nas versões do
`Gemfile.lock`, as gems travadas e o Lychee usado pelo Dockerfile, sem precisar
de Docker. Execuções posteriores reaproveitam as ferramentas e gems instaladas.
Não há hook de resume: este projeto não precisa de autenticação ou reparos ao acordar.

Para preparar manualmente o ambiente, execute `./.agents/setup`. As ferramentas
ficam disponíveis em novos shells de login dentro do repositório.

* Build: `bundle exec jekyll build`
* Links: `make links`
* Preview supervisionado e acessível pelo portal: `amp orb services ensure`

O preview é declarado em `.amp/services.yaml`; o setup não inicia servidores.
O tema remoto do Jekyll é baixado durante o build, que ainda precisa de acesso à rede.
