---
layout: post
title: Documentação
date: 2012-04-02
category: PHP, jardineiro
published: false
---

"Documentação em um projeto é algo essencial". É um conhecimento bem comum, mas
não mais comum do que o "documentar qualquer coisa é um saco". No meio desse conhecimento
todo estamos nós. Produzindo código.

O resgate do README
-------------------

Dentre todas as muitas contribuições ao mundo open source, devemos ao GitHub o
resgate do README como uma documentação realmente útil de novo.

Decisivo para este resgate foi colocar nele uma marcação humana muito mais eficiente
e organizada do que um simples *plain/text*.

A API
-----

Já que documentação é um saco, vamos direto para o mínimo necessário, a API. A API
de uma aplicação são os pontos de entrada dela. De um site são as URLs, de uma
classe os métodos públicos e de um componente os métodos públicos das classes
deste componente.

O mínimo a ser documentado é isso. Hoje temos um ótimo candidato para fazer isso,
o PHPDoc. Ele passou um tempo esquecido pela falta de uma alternativa (decente) ao
parsing e geração da documentação, problema que a algum tempo não temos mais.

Bom código
----------

Podemos discutir durante décadas e ainda não chegar à conclusão nenhuma. Se você
tem alguma dúvida disso, assine a lista do *PHP Standards Group* e leia  o quão 
longa e cansativa ela pode ser.

Vamos para o mínimo de novo: testes. Já que bom código é muito relativo vamos para
outra abordagem: qual o código que conseguimos conviver? Código testado.
Algum ser (humano) pode produzir a maior atrocidade da terra, mas se este possuir
testes então conseguimos ignorá-los.

