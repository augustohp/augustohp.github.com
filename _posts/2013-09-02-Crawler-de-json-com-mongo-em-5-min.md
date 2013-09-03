---
layout: post
title: Um crawler em 5 minutos
categories: [hacks, unix]
---

Eu não sei se é uma prática geral mas eu gosto de ter dados guardados pra quem sabe, algum dia, dominar o mundo?!
Há muito tempo não via uma API que me desse vontade de sugar, vou mostrar o que fiz pra baixar todo conteúdo JSON de uma API pública (que não me impediu de fazer isso).

## Requisitos

Já adianto que eu não fiz nenhum milagre, aqui está tudo o que precisa pra esse crawler:

* [MongoDB](http://www.mongodb.org/)
* [Bash](http://en.wikipedia.org/wiki/Bash_%28Unix_shell%29)
* [cURL](http://curl.haxx.se/)

## O Crawler

A [api](http://mtgapi.com/) em questão tem informação de [quase](https://news.ycombinator.com/item?id=6300576) todos os cards do [Magic: The Gathering](http://www.wizards.com/Magic) em formato [JSON](http://json.org) (por isso o MongoBD).

Um dos *endpoints* é `http://mtgapi.com/api/v1/fetch/id/{id}` onde o `{id}` pra mim foi um auto incremento até o infinito. 

O crawler que usei consiste de uma linha, abaixo vai uma versão extendida (mais fácil de ler):

<pre class="language-bash">
#!/bin/bash
URL="http://mtgapi.com/api/v1/fetch/id/"
for ID in {1..999}; do
    result=$(curl --get --silent -H "User-Agent: BadassBash 0.0.1 (Yep, another crawler)" "${URL}/${ID}" 2> crawler.err)
    echo $result | mongoimport localhost -d magic -c cards
done;
</pre>
