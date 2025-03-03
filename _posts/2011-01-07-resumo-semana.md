---
layout: post
title: Resumo da Semana PHP (Jan \#1)
date: 2011-01-07
category: PHP,Resumos
---

Esse é o primeiro post de uma série que pretendo fazer. A proposta é
simples: resumir a semana do PHP no mundo neste post. Se saiu algo de
interessante que não está aqui, por favor me evise no
[@augustohp](https://twitter.com/augustohp) ou deixe um comentário e eu
atualizo o post.

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
-   [**Phake**](https://digitalsandwich.com/archives/84-introducing-phake-mocking-framework.html):
    Uma nova ferramenta para mocking, baseada no Mockito do Java. Sua
    sintaxe é mais intuitiva do que a ferramenta de Mock nativa do
    PHPunit. Se você gostar dela, deveria dar uma olhada também no
    [Mockery do Padraic](https://github.com/padraic/mockery).
-   [**Drupal 7**](https://drupal.org/drupal-7.0): Saiu a nova major
    version do Drupal depois de quase 3 anos de desenvolvimento. O
    Drupal dispensa apresentações, mas se você não conhece;
    definitivamente deveria dar uma olhada.

## Posts

-   [Status da integração contínua no
    PHP](https://web.archive.org/web/20100912001907/www.littlehart.net/atthekeyboard/2010/09/07/twitter-asks-continuous-integration-landscape-for-php-developers/):
    Este post descreve (do ponto de vista do autor), qual o estado atual
    de quem utiliza integração contínua no dia a dia desenvolvendo
    aplicações PHP. Se você quer começar a ter algum contato com isso, o
    post vale a leitura.
-   [Crie seu próprio widget de Twitter][1]:
    É uma série de 3 posts que mostra como você pode interagir com a API
    do Twitter. Os códigos utilizados não são algo que você deveria
    seguir como exemplo de bom código; mas se você não conhece a API do
    Twitter e está começando com Orientação a Objetos, essa série pode
    te ajudar um pouco.

[1]: https://web.archive.org/web/20110304231046/blogs.sitepoint.com:80/2011/01/05/create-your-own-twitter-widget-1/
