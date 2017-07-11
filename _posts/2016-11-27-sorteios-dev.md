---
title: Sorteando coisas como um dev
layout: post
date: 2016-11-27
category: unix
---

Já participou de algum tipo de sorteio em eventos de desenvolvimento?
Viu o [random.org][] sendo usado ou um programa parecido? Já pensou [na shell
como um interpretador][1] e que você poderia usar simplesmente ela?

Precisamos de algumas coisas pra fazer isso acontecer:

1. Um arquivo com a lista a ser sorteada. Uma pessoa por linha.
1. Um comando para retornar um número randômico, dentro de limites.
1. Um comando pra retornar um número específico de uma linha.

O número randômico é simples. O *bash* tem uma variável `$RANDOM` que você pode
usar, só precisamos delimitar um limite inferior e um superior. Nosso limite
inferior é 1, enquanto o superior é o número de linha do arquivo (no nosso
exemplo `/tmp/file`).

    $ wc -l /tmp/file.txt
        312 /tmp/file.txt
    $ wc -l /tmp/file.txt | awk '{print $1}'
    312

Acima, temos o `wc` imprimindo o número de linhas do arquivo, junto com o nome
dele. Como queremos só o número de linhas, usamos o `awk` pra retornar só a
primeira parte do *output* do `wc`.

    $ echo $RANDOM    
    31938
    $ upper_limit=312
    $ lower_limit=1
    $ echo $(( ($RANDOM % $upper_limit) + $lower_limit ))
    198

Acima vimos como gerar um número randômico entre dois limites. Pro limite
superior usamos o resto da divisão entre o `número randômico` e o `limite
superior`, enquanto que pro inferior utilizamos uma soma. Numa shell, se você
precisa de [expensão aritimética][2] usamos `$(( 1 + 1 ))`.

    $ random_line=198
    $ awk "NR==${random_line}" /tmp/file.txt
    john@doe.com

O `awk` é uma linguagem inteira, evitando entrar em muitos detalhes, a variável
`NR` possui o número de registros que o `awk` interpretou até agora. Por padrão
um registro é uma linha, então nosso programa `awk` está avaliando se o registro
atual é o número randômico que passamos, caso sim ele imprime a linha.

Se juntarmos tudo isso num script um pouco melhor, nos preocupando com a leitura
e manutenção dele:

    #!/usr/bin/env sh
    # Prints a random line from a file

    lines_on() {
        file=$1
        wc -l $file | awk '{print $1}'
    }

    random_until() {
        max=$1
        min=1
        echo $(( ($RANDOM % $max) + $min ))
    }

    print_line_in_file() {
        file=$1
        line=$2
        awk "NR==${line}" $file
    }

    if [ -z "$1" ]
    then
        echo "Usage: $0 <file>"
        exit 2
    fi

    print_line_in_file $1 $(random_until $(lines_on $1))

O importante não é colocar isso num script e lembrar que ele existe, mas
transformar o uso dos comandos acima em memória muscular. Acredite, todos eles
são úteis no dia a dia.

Quer uma lição de casa bacanuda? Vamos evitar repetir membros já sorteados?

[1]: http://example.org "Como ser um desenvolvedor melhor em 5 min"
[2]: http://www.tldp.org/LDP/abs/html/arithexp.html

<!--
vim: spell spelllang=pt
-->
