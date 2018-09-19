---
layout: post
title: MVC - Você está fazendo errado
date: 2011-07-28
category: PHP, Jardinagem
---

Este post poderia se chamar também: "Porque o Zend Framework não possui
Models". Mas ele se chama "MVC - Você está fazendo errado". Porque você
está fazendo errado.

Existem algumas ressalvas que quero fazer antes de mais nada. Primeiro,
eu não sou um Engenheiro de Software, sou um jardineiro. Segundo, eu
tenho certeza de que se você utiliza MVC, você está o utilizando de
forma errada.

Antes de me criticar, leia tudo. ;)

## Somos jardineiros

Desenvolvimento de software não é uma ciência exata como é a engenharia.
Hoje já é bem grande o número de pessoas que sabe que é muito mais
importante saber reagir a uma mudança ou problema do que seguir o plano
inicial.

Um software nunca está pronto, nunca planejamos um software nos mínimos
detalhes como em uma casa e entregamos exatamente o que foi planejado.
Não somos engenheiros, somos todos jardineiros.

Planejamos onde colocar as coisas, o que usar, e temos que tomar conta
do nosso jardim a fim de manter ervas daninhas longe. Manter um jardim é
uma tarefa constante, assim como o desenvolvimento de um software.

Somos todos jardineiros. Para ser um bom jardineiro, basta apenas
aceitar isso.

## O famoso MVC

Todo esse lenga lenga, para chegar ao MVC, porque? Porque é mais que
difundido que desenvolver um software utilizando a arquitetura de MVC
traz pra você muita vantagem, controle e isolamento de partes críticas
do software.

O MVC é bacanudo. Não vou discutir isso aqui. Mas antes de mais nada,
vamos lembrar o que significa cada letra do MVC. Serei breve - prometo -
já que acho que todo mundo sabe o que significa cada uma:

### M: Model

A parte de modelo deve conter a regra de negócio de sua aplicação. A
regra de negócio de uma aplicação é a parte essencial dela, é por isso
que você está criando uma aplicação, todo o resto; é resto.

### C: Controller

O controller deve fazer a ponte entre a Model e as Views, deve fazer a
validação dos dados de entrada, mandar pras Models correspondentes e
devolver dados para View.

### V: View

A camada de apresentação não é nada além disso. É o HTML com o conteúdo
que o Controller passou pra ela.

## O infame MVC

Você já usou MVC? Se já, você provavelmente usou errado. Já repeti isso
algumas vezes e a essa altura você deve estar ofendido já. Que bom!
Assim você (provavelmente) nunca mais vai esquecer disso.

Qual a parte mais importante de uma aplicação? Regras de negócio,
controle e validação ou apresentação dos dados?

Não se engane, apesar da apresentação ser importante ela nada é sem a
inteligência das regras de negócio. As regras de negócio são o mais
importante porque é ali que está todo o esforço de programação. É pra
ela que você contrata bons programadores!

Ótimo, agora sabemos qual a parte mais importante do MVC. Se formos
pensar em um bolo, o Model é a base de tudo e o Controller o recheio que
une as Models e as Views. Um belo bolo!

## Um bolo não tão belo assim ...

A parte mais importante desse bolo é a base, a Model. Agora eu pergunto:
Qual camada do bolo é maior na sua aplicação? Model, Controller ou View?

Onde você passa maior parte do tempo programando, corrigindo bugs e
implementando novas funcionalidades?

Infelizmente a resposta da maioria pra esta pergunta é "Controller".
Revisamos o que o controller deve fazer, ele deve somente dar *input* de
dados validados na Model, pegar o *output* delas e enviar como *input*
pras Views.

Onde a coisa saiu errada pra fazer todo mundo sair programando tudo
dentro dos controllers? Porque tão pouca gente se atentou a isso até
agora?

## A culpa é dos frameworks

Frameworks como CakePHP, CodeIgniter e Kohana trazem uma funcionalidade
milagrosa (o certo seria ler "preguiçosa"): Active Record.

Não quero nem entrar no mérito de que elas implementam esse Design
Pattern de forma errada, mas quero entrar no mérito de que elas usaram o
Active Record, e chamaram tudo que faz uso desse pattern de Model.

O mundo? Foi atrás, afinal esses são os frameworks mais utilizados de
PHP hoje. Pedir que alguém simplesmente estude design patterns e veja o
quão errado está tudo é demais quando a pessoa utiliza um framework
basicamente só porque ele faz as operações de banco de dados pra você.

Doa a quem doer, mas essa é a verdade do PHP hoje. A grande maioria
utiliza ferramentas sem nem entender direito o que está fazendo.
Acreditam no mundo do Harry Potter e acham que a qualquer momento o
Voldemort vai sair do código caso ele abra o código de uma classe que
não deveria.

A bem da verdade, se qualquer um tivesse aberto meia dúzia de classes
quaisquer desses frameworks, eu tenho certeza que eles não estariam
utilizando eles.

## Porque o Zend Framework não possui Models

Porque é impossível abstrair toda regra de negócio possível e
imaginável! Simples, não?

A regra de negócio é o seu negócio, é o seu trabalho, é o seu
planejamento!

O que o ZF faz por você é dar uma PUTA PENCA de componentes pra você
usar e abusar. Cabe a você desenvolver sua biblioteca e sua aplicação.

### Como eu costumo fazer

Não que isso seja o mais correto, ou a única forma de fazer; mas é como
me sinto confortável utilizado o Zend Framework e como acho que as
coisas ficam semanticamente interessantes:

    /application
    /application/configs
    /application/layouts
    /application/languages
    /application/modules
    /application/modules/default
    /application/modules/default/entities
    /application/modules/default/controllers
    /application/modules/default/views
    /library
    /library/Zend
    /library/MyApp
    /public
    /tests

É basicamente isso. Dentro do diretório de *entities* eu coloco as
entidades do **Doctrine**, dentro de /library/MyApp eu coloco todas as
classes que compõem a regra de negócio da minha aplicação e dentro de
/tests os testes unitários.

## Zend Framework, a ressalva

Eu costumo dizer isso bastante, mas repetir nunca é demais. O Zend
Framework tem suas falhas, mas no geral ele é um ótimo framework. Hoje é
minha escolha pra qualquer projeto, mas ele tem um porém: a documentação
dele é fraca. Bem fraca. Os componentes até são relativamente bem
documentados de forma isolada, mas quando se trata de usar tudo junto o
que resta é você e a penca de tutoriais mostrando os mais diversos
absurdos por aí.

Você provavelmente vai me perguntar um bom material sobre Zend
Framework, e eu vou te deixar mais puto e responder que não existe.

O melhor material sobre Zend Framework que existe hoje é o conhecimento
sobre Deisn Patterns, Domain Driven Development e o próprio código do
ZF. Fora isso, tome muito cuidado com o que você lê.

Pronto, fique a vontade pra me esculachar agora =D

Até a próxima, ou não! ;)

PS: A quem quiser algo mais concreto de Zend Framework, o
[@guilhermeblanco](http://twitter.com/guilhermeblanco) tem um projeto
que é o esqueleto de uma aplicação em Zend Framework e Doctrine 2. Mesmo
que você não use o Doctrine 2, o projeto vale uma olhada:
https://github.com/guilhermeblanco/Zend1-Doctrine2-Skeleton
