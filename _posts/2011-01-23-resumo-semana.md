---
layout: post
title: Resumo da Semana PHP (Jan \#3)
category: PHP
published: true
---

Continuo seguindo com o resumo semanal do que acontece no PHP no mundo.
Se você não tem muito tempo pra se atualizar, eu invariavelmente leio
(tento) tudo que posso e tentarei manter essa assiduidade até o final do
ano, espero que me ajudem com isso.

## Campus Party

Caso você viva em outro planeta e chegou a esse blog por acaso, essa
semana aconteceu a Campus Party Brasil 2011. Em sua quarta edição no
Brasil as melhoras da organização são óbvias, apesar de alguns pecados
cometidos.\
Sim, faltou luz. Algumas vezes. Isso é chato? Extremamente, mas acredito
que com certeza ano que vem não teremos mais esse tipo de problema.\
Afinal, o que você faz na Campus Party?\
Eu vou pra encontrar pessoas que gostaria de ter perto o ano todo, mas
não tenho. Pessoas que contribuem muito com a linguagem e a web em
geral. Conversar com elas vale muito mais do que a leitura de uma dúzia
de livros.

Eu e o [Dohms][1] tivemos a oportunidade de
palestrar de novo na Campus Party. Ele palestrou sobre como você pode
crescer utilizando PHP, como você pode trilhar seu caminho nessa
linguagem que cresce a cada dia; já eu ataquei os quatro principais
frameworks do mercado, tentei ser o mais imparcial possível. As
apresentações seguem abaixo:

<div style="width:425px" id="__ss_6619692">
<strong style="display:block;margin:12px 0 4px"><a href="https://www.slideshare.net/rdohms/trilhando-o-caminho-php-20-campus-party-2011" title="Trilhando o Caminho PHP 2.0 - Campus Party 2011">Trilhando
o Caminho PHP 2.0 - Campus Party
2011</a></strong><object id="__sse6619692" width="425" height="355"><param name="movie" value="https://static.slidesharecdn.com/swf/ssplayer2.swf?doc=trilhando-2-0-cparty-110118193031-phpapp02&rel=0&stripped_title=trilhando-o-caminho-php-20-campus-party-2011&userName=rdohms" /><param name="allowFullScreen" value="true"/><param name="allowScriptAccess" value="always"/><embed name="__sse6619692" src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=trilhando-2-0-cparty-110118193031-phpapp02&rel=0&stripped_title=trilhando-o-caminho-php-20-campus-party-2011&userName=rdohms" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="355"></embed></object>

<div style="padding:5px 0 12px">
Veja mais apresentações do
<a href="https://www.slideshare.net/rdohms">Rafael Dohms</a>.

</div>
</div>
<div style="width:425px" id="__ss_6643165">
<strong style="display:block;margin:12px 0 4px"><a href="https://www.slideshare.net/augustopascutti/campus-party-frameworks-php" title="Campus Party - Frameworks PHP">Campus
Party - Frameworks
PHP</a></strong><object id="__sse6643165" width="425" height="355"><param name="movie" value="https://static.slidesharecdn.com/swf/ssplayer2.swf?doc=frameworks-110120123318-phpapp01&rel=0&stripped_title=campus-party-frameworks-php&userName=augustopascutti" /><param name="allowFullScreen" value="true"/><param name="allowScriptAccess" value="always"/><embed name="__sse6643165" src="http://static.slidesharecdn.com/swf/ssplayer2.swf?doc=frameworks-110120123318-phpapp01&rel=0&stripped_title=campus-party-frameworks-php&userName=augustopascutti" type="application/x-shockwave-flash" allowscriptaccess="always" allowfullscreen="true" width="425" height="355"></embed></object>

<div style="padding:5px 0 12px">
Veja mais apresentações
<a href="https://www.slideshare.net/augustopascutti">minhas </a>.

</div>
</div>

## Desenvolvimento do PHP

-   **Novas versões**: Tivemos o lançamento de uma nova *"minor"*
    version, tanto pra árvore 5.2 quanto pra 5.3. A correção em questão
    é sobre uma brecha de segurança na conversão de *strings* em
    *doubles*. [Mais
    informação](https://www.php.net/archive/2011.php#id2011-01-06-1)
-   **Perfomance Hash**: Um pessoal fez um profilling do código atual do
    PHP e concluiu que era possível melhorar as funções de hash
    (MUUUUITA coisa depende delas). Fizeram um patch, enviaram e agora
    outras pessoas estão melhorando e garantindo que as coisas funcionem
    como deveriam. Software Livre é isso. [Mais
    informações](https://web.archive.org/news.php.net/php.internals/51158)
-   **Engraçado**: ~~A um ano atrás~~ Há um ano alguém abriu um bug no
    PHP porque a função number\_format() não estava retornando mais 0
    (zero) e sim *null* após a atualização para o PHP 5.3.1. Ninguém
    mais nem menos que o *Rasmus Lerdorf* respondeu o bug pacientemente,
    mas a conversa vale a pena ser lida. [O santo
    bug](https://bugs.php.net/bug.php?id=50696)

## Ferramentas

-   [**Phake**](https://digitalsandwich.com/archives/84-introducing-phake-mocking-framework.html):
    Uma nova ferramenta para mocking, baseada no Mockito do Java. Sua
    sintaxe é mais intuitiva do que a ferramenta de Mock nativa do
    PHPunit. Se você gostar dela, deveria dar uma olhada também no
    [Mockery do Padraic](https://github.com/padraic/mockery).
-   [**Drupal 7**](https://drupal.org/drupal-7.0): Saiu a nova major
    version do Drupal depois de quase 3 anos de desenvolvimento. O
    Drupal dispensa apresentações, mas se você não conhece;
    definitivamente deveria dar uma olhada.

[1]: https://web.archive.org/web/20121106162819/www.rafaeldohms.com.br:80/
