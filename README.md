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
ficam disponíveis em novos shells de login dentro do repositório e seus
subdiretórios. O setup reposiciona somente o hook deste projeto no final de
`~/.bash_profile`, depois do carregamento de `~/.env` pelo Amp, que pode
sobrescrever o `PATH`. O hook não ativa Ruby fora do repositório.

* Build: `bundle exec jekyll build`
* Links: `make links`
* Preview supervisionado e acessível pelo portal: `amp orb services ensure`

O preview é declarado em `.amp/services.yaml`; o setup não inicia servidores.
O serviço usa `$HOME/.local/bin/mise exec` explicitamente, com Ruby e Bundler
derivados do `Gemfile.lock`, sem depender do `PATH` herdado ou da ordem do profile.
Se o Amp acrescentar outro reset de `PATH` depois do hook em uma atualização do
orb, execute o setup novamente antes de usar `bundle` em shells de login.
O serviço de preview continua independente desse hook; o setup não altera
`~/.env` nem reinicia o processo do Amp que já está em execução.
O tema remoto do Jekyll é baixado durante o build, que ainda precisa de acesso à rede.

### Origens no relatório de links

O workflow Link Health mantém o JSON do Lychee como fonte dos resultados.
Depois da checagem, `bin/link-report-sources.py` faz um build de produção seguro
com o bundle travado, fora da árvore checada. O Jekyll resolve as URLs publicadas;
o HTML renderizado fornece os IDs reais dos títulos.

Os links de origem apontam à seção precedente mais próxima, não à ocorrência
exata. Antes da primeira seção, o título do post (`#page-title`) é usado quando
existe. URLs repetidas listam todas as seções correspondentes, sem tentar inferir
uma ocorrência a partir do único `span: {line, column}` do Lychee. Sem título
precedente, ou quando a URL não aparece no HTML, o destino é a página sem fragmento.
Arquivos não publicados (ou falha no build auxiliar) recebem um link ao código
no commit checado, com a linha do span quando disponível. Uma falha de build
continua deixando o job vermelho, mas não impede o resumo e a atualização da issue.

Regressão local: `python3 bin/test-link-report-sources.py` (requer o bundle e
Lychee 0.24.2 do setup). Usa Jekyll real e um servidor local 404 para validar spans,
links repetidos, referências, escapes, datas, categorias e permalinks. Executa o
script do workflow com API simulada, sem escrever em issues do GitHub.

## Comentários

O tema usa `disqus.shortname: augustopascuttisblog`, não `comments` na configuração
global. Essa configuração foi removida em [fevereiro de 2025](https://github.com/augustohp/augustohp.github.com/commit/daff4e2d0bf8dd67e91a5ef9ae2404d5a9bd9694),
antes da migração de dependências e publicação via Actions (#76).

`_includes/disqus-comments.html` preserva as URLs e os identificadores HTTP
anteriores à migração para HTTPS. Esses valores são chaves de discussão no
Disqus, não requisições HTTP: páginas, canonical e script continuam em HTTPS.
Não altere o fórum, as chaves ou os permalinks sem conferir as discussões
existentes no Disqus; isso pode separar os comentários históricos.

Os comentários aparecem somente em builds de produção, como no Pages:
`JEKYLL_ENV=production bundle exec jekyll build --safe`. O preview de
desenvolvimento não carrega o Disqus. Para desabilitar em um post específico,
use `comments: false` no front matter. `python3 bin/validate-site.py` valida
o build de produção, incluindo o fórum e as chaves históricas.
