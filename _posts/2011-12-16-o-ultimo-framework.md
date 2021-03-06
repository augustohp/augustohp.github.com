---
layout: post
title: O último framework
date: 2011-12-16
category: PHP, jardineiro
---

Um framework tenta suprir às necessidades da maioria dos desenvolvedores
criando uma camada de abstração que facilita a vida deles no dia a dia.\
Não vou contestar a prática de abstrair algo, pelo contrário, acho ela
extremamente necessária e vou incentivá-la. Só vou contestar como isso
vem sendo feito até agora.

## Qual o melhor framework existente hoje?

Responder uma pergunta com outra é algo ridículo de se fazer, mas nesse
caso algo extremamente justificável. Porque você acha a resposta à essa
pergunta importante?

Julgo eu que essa pergunta é feita a fim de saber qual o framework que
mais vai ajudar você a fazer o que você quer no dia a dia. Se perguntada
de outro jeito, seria algo como: Qual o framework que mais vai me
ajudar?!

Hoje a resposta seria o Symfony 2. Depois de demorar mais do que uma
gestação humana para ser feito, testado e liberado com uma API estável
ao "público", eu não chamaria o projeto de um sucesso completo. Mas um
sucesso, sem sombra de dúvida ele é.

O Symfony 2 é extremamente produtivo, possui integrado ferramentas muito
competentes no que fazem e é bem documentado. É relativamente rápido,
possui um sistema de plugins (bundles) e além de possuir um praticamente
popstar como mantenedor, te ajuda como nenhum outro framework com os
erros.

Poderia analisar cada framework, com os prós e contras de cada um agora,
e ainda assim, o Symfony 2 ganharia dos demais em um tipo de média.
Agora uma pergunta interessante que quase nenhum desenvolvedor faz é:

### Existem motivos para não escolhê-lo?

Obviamente que sim, mas estes motivos não estariam ligados somente ao
Symfony, e sim a praticamente qualquer outro framework que você citar.

Tente criar uma página "Sobre", só com um textinho bonito. O resultado
provavelmente seria uma classe para responder à URL (Controller) e uma
View, quando no caso a única coisa que precisa existir de fato é o
arquivo HTML que é a View.

Em vários outros casos o framework acrescenta uma complexidade
desnecessária, o que resulta (ao invés do que se espera) em mais tempo
para desenvolver algo. A complexidade é tão grande que uma ótima
decumentação é requisito mínimo de um bom framework. No fim (ou hoje
mesmo) uma série de auto proclamados profissionais sequer sabem a
diferença entre o framework e a linguagem.

Todo framework possui uma curva de aprendizado, por menor que ela seja.
Todo framework possui uma limitação, não importa o quão abstraídos são
os domínios. Nenhum framework é tão bem documento quanto o PHP e nenhum
framework tem uma base de uso tão grande quanto o PHP.

Passou da hora de copiarmos outras linguagens, nós já dominamos a
internet. Temos uma das maiores (senão a maior) comunidade Open Source,
somos um dos maiores (senão o maior também) casos de sucesso do modelo
Open Source e ainda achamos que o Rails ou o Java são uma boa idéia.

## O PHP

É a linguagem mais utilizada na internet não por causa do nome, do
mascote ou de um framework. Ela o é porque é multiparadigma. Ela sai do
caminho do desenvolvedor.

Já temos ótimos frameworks para praticamente todas as necessidades e
gostos, mas somos uma linguagem incrivelmente pobre em termos de
componente. Praticamente todo framework tem e depende muito de um
sistema de cache, mas não temos nenhum componente de cache bom,
indepente dos frameworks.

Temos MVC em todos os frameworks, mas nenhum componente que forneça uma
estrutra pra isso de forma razoável a ser utilizada por todos os
frameworks. Autenticação sem um framework deve ser feita na mão,
praticamente todo site hoje tem autenticação e não existe nenhum
componente de autenticação escrito em PHP.

Os frameworks deixaram de ser uma opção, viraram uma prisão. Uma
dependência para muitos desenvolvedores e para a comunidade em geral.
Temos ótimos frameworks se comparados com outras linguagens e eles não
são poucos, mas poucos componentes bons quando se trata de uma tarefa em
específico.

## A filosofia unix

Faça pouco, mas faça isso como ninguém. Seja o melhor do melhor do mundo
em dizer "Oi" como quem viu um pato molhado vestindo capa de chuva
amarela sem a bota direita.\
Essa é a filosofia que fez um sistema operacional ser o melhor pedaço de
software do mundo durante muitos anos consecutivos, e o melhor: livre e
gratuito.

## O último framework

Não se trata de um framework propriamente dito, muito menos se trata de
um framework que torne desnecessário qualquer outro. Se trata de um
conjunto dos melhores componentes existentes para as mais diversas
tarefas que possamos precisar.

Ele não precisa de documentação, ele não precisa ser utilizado de forma
completa. Ele sai do caminho do desenvolvedor, mostrando a ele quais são
as melhores ferramentas para serem utilizadas contra cada problema. Cada
componente faz o que deveria fazer e ponto, assim como um comando no
terminal faz seu trabalho.

## "Como sair do caminho do desenvolvedor" ou "O que faz um bom componente" ?

Diga não ao parnasianismo do software. Precisamos da simplicidade se
quisermos manter nossa sanidade. O que é mais simples do que pegar um
problema e resolvê-lo? A documentação? Métodos pública de uma classe
deveriam ser mais do que suficientes, caso o problema seja um pouco
maior do que o esperado, aquele **README** espertinho contendo alguns
exemplos curam até câncer se você quiser.

-   Quase todo mundo usa o Git, digo, o GitHub. Resistir é inútil.
-   Utilize os padrões. Se classes são necessárias, a PSR \#0 foi criada
    para isso.
-   Temos um padrão de código que é praticamente do próprio PHP, a da
    Pear ou da Zend.
-   Temos um gerenciador de pacotes muito bom, tanto para código PHP
    quanto para extensões em C, a Pear.
-   Temos uma ótima ferramenta a candidata única de testes unitários, o
    PHPUnit e se não agradar o PHP tem a própria ferramenta de testes, o
    PHPT.

## Quais os componentes precisamos?

Pracisamos de praticamente tudo, sério. O que temos hoje ou é
demasiadamente complexo, ou não é mais mantido, não é documentado ou não
é utilizado como componente (faz parte de um conjunto maior).

-   Autenticação
-   Configuração
-   Relatórios
-   Cache
-   Parser/Tokenizer
-   Active Record (Para os fan boys de Rails, quem sabe ...)
-   Requisição/Resposta (Ex: HTTPKernel do Symfony)
-   Gerência de Banco de Dados (Migrations)
-   Gerência de configuração

E mais qualquer coisa que você tenha feito mais de uma vez. Ajuda nos
comentários, manda um pacote ou sugestão de componentes que você acha
que é simples o suficiente para o que você julga ser o idel **Último
Framwork**.

Eu comecei um pet project cujo meu objetivo é manter simples e sempre
utilizando o máximo de componentes que eu puder. Ele começou e isso é o
que importa, não esta nem um pouco intuitivo (ainda) eu acho, mas
críticas são bem vindas, sempre. Espero elas no
[GitHub](https://github.com/augustohp/Eight).
