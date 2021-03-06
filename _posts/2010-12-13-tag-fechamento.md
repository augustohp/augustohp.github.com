---
layout: post
title: Omissão da TAG de fechamento do PHP
date: 2010-12-13
category: PHP
---

Há um tempo atrás o dia se arrastou um tanto quanto divertido no twitter.
Uma série de pessoas entraram na seguinte discussão:

> Utilizar a tag de fechamento do PHP (`?>`) é uma boa prática ou não?

As respostas (pra minha supresa) foram diversas, mas basicamente duas:

-   Sim, caso ela não seja necessária, não utilizar é uma boa prática.
-   Não. Ela é opcional e portanto não precisa ser omitida.

## O problema

Eu tenho minha posição, mas antes de apresentá-la, vamos ao porquê da
discussão. Ao omitir (não usar) a tag de fechamento do PHP, você faz com
que o PHP trate os espaços e as quebras de linha como caracteres não
significativos e nada acontece. Se você não omitir e fechar a tag no
final do script, o que acontece é que tudo que vier fora dos \<?php ...
?\> é diretamente jogado para o navegador. Qual o problema?

O problema é que para enviar uma informação ao navegador, o Apache
precisa antes enviar o cabeçalho HTTP; mas existem funções do PHP que
usam esse cabeçalho, como exemplo o session\_start(), a header(), etc
...

O PHP ignora automaticamente o caracter de quebra de linha logo depois
de sua tag de fechamento, se esse caracter existir, mas se houver outro,
ou um espaço, bum. Problema.
Imagine se isso acontece no seu arquivo de configuração? Você fecha o
PHP dele e logo depois vem alguém, ou você mesmo, e dá alguns enters ou
algum espaço depois da tag de fechamento. O que acontece? Você muito
provavelmente vai passar um bom tempo tentando descobrir onde está o
problema que impede você de usar algumas funções que precisem moficar o
cabeçalho do PHP.

## Coclusão

Evite utilizar a tag de fechamento do PHP quando não for necessário.
Esqueça a discussão de boas práticas ou não e faça o que for melhor pra
você: evite fechar a tag e poupe-se do famoso "*Headers already sent*".
