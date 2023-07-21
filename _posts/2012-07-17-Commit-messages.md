---
layout: post
title: Mensagens Commit
category: Desenvolvimento
---

Espero (sinceramente) que você use algum sistema de controle de versões. A idéia aqui
é (como o título sugere) expressar a importância das mensagens de commit em um
projeto.

Nossa função
------------

Expressar nosso objetivo como profissionais é sempre algo delicado de se fazer,
ainda mais algo genérico. Provavelmente essa minha definição mude com o tempo, 
mas atualmente ela seria algo assim:

    "Arquitetar um conjunto de necessidades com a finalidade de evoluir da maneira
    mais simples e óbvia possível."

A *expressão* tem duas partes, a primeira convém a evolução lógica e inexorável
de um software que (assim como praticamente tudo) surge sempre de uma necessidade.
Não acho que exista nada de muito delicado nem questionável aí.

A segunda parte fala de simplicidade. O ponto delicado aqui é *entender* o que é
*simplicidade*.

Simplicidade
------------

É bem natural pensar que qualquer coisa "*grande*" seja complexa, assim como é
natural ver algo simples e não esperar resultados magníficos.

Toda uma genialidade é necessária para abstrair algo complexo de maneira simples.
Exemplos disso são: a teoria da gravidade e consequentemente da relatividade e a
web.

A simplicidade é importante porque ela é extremamente acessível. Não é necessário
muito estudo nem habilidade pra entender algo simples, seja qual for esse entendimento.
Entender "*algo*" não é tão importante e essencial quanto consumir os benefícios
desse mesmo "*algo*".

Simplicidade em software é importante por diversos motivos, o que nos interessa
aqui é o ponto específico de que o software precisa ser mantido. Tornar essa 
manutenção uma tarefa simples é uma obrigação e ferramentas pra isso existem várias:
comentários simples, PHPDoc, padrões de codificação, Testes Unitários, 
Testes de Comportamento e (porque não) **mensagens de commit**.

Mensagens de commit
-------------------

Todo código que produzimos é fruto de algum pensamento lógico, por mais ilógico
que ele pareça. Tentamos deixar esse *fruto* o mais simples possível de se entender,
essa simplicidade é grande responsável pela evolução do software como produto final.

Porém o código tem um limite. Comentários no meio dele mais atrapalham do que ajudam
quando ele é simples o suficiente, eles só são necessários quando o código é
extremamente ineficiente em expressar à um humano seus objetivos.

Lembre-se que (se) você escreve códigos numa linguagem de alta abstração para 
humanos entenderem e não para máquinas. O problema de comunicação com a máquina
já esta resolvido em camadas abstratas mais baixas.

Porém comentários em códigos tem problemas, o mais crítico é a falta de ordem
cronológica neles. Algo que uma mensagem de commit faz naturalmente. E como saber
à que pedaço de código aquela mensagem de commit pertence? Procure por **blame**
no seu gerenciador de versão preferido.

A mensagem de commit deve expressar o objetivo que aquele conjunto de mudanças
têm de maneira clara e objetiva, ela é uma ferramenta fenomenal de discussão
muito pouco utilizada.

Uma mensagem de commit digna de entrar no controle de versões deve responder à
algumas perguntas:

* Qual problema ele resolve
* Como o problema é resolvido
* Se necessário, o porquê determinada solução foi escolhida

Ela é a melhor forma de comunicação para um desenvolvedor dentro de um projeto.
Esqueça os *bug trackers*, o GitHub, e-mail, ferramentas de review de código e
demais soluções. As mensagens de commit não substituem elas, mas são a melhor
ponte de comunicação entre os desenvolvedores e códigos já que além de tudo, estão
ligados à eles. Virtualmente (ou fisicamente se você encarar que o sistema de arquivos
é algo físico) e cronologicamente.

Quer saber o que se passava na cabeça de um desenvolvedor ao criar, alterar ou
remover linhas de código? O que você deve procurar como resultado no código e
como ele vai se comportar? As mensagens de commit são ótimas alternativas.
indubitavelmente superiores aos comentários dentro do código.

Exemplo
-------

O [debian][] recentemente (na *Jessie*) trocou o gerenciador de janelas padrão do
[gnome][] pro [xfce][]. O anúncio pode ser lido, juntamente com as mudanças na
distribuição diretamente [na mensagem de commit][commit].

A mensagem de commit possui:

- A motivação da mudança.
- Qual foi a mudança, além do *diff* de código deixar ela bem explícita.
- Quais os casos em que esse commit pode ser revertido.
- Qual o impacto do commit, para os usuários. (O valor entregue)

Hoje, segundo meus julgamentos, ele já é um excelente commit mas daqui alguns 
anos ela pode muito bem ser usada (também em conjunto com as mensagens de commit
futuras relacionadas aos mesmos arquivos) pra contar a história do projeto: as decisões e 
o porquê delas. Evitando erros futuros ou estimulando decisões parecidas.

Conclusão
---------

Espero ter conseguido mostrar a importância que uma simples mensagem de commit
tem. O quão simples e vital é ter isso em qualquer projeto.

Se tudo for como eu espero, todas suas próximas mensagens de commit serão algo
que valha ser lido ao invés de ser algum pedaço de texto que alguma ferramenta
estúpida requer repetidamente a fim de fazer algo.

[commit]: https://salsa.debian.org/installer-team/tasksel/-/commit/dfca406eb694e0ac00ea04b12fc912237e01c9b5
[respect]: https://github.com/Respect "GitHub: Componentes do Respect"
[foundation]: https://github.com/Respect/Foundation "GitHub: Repositório do Respect/Foundation"
[nick]: https://github.com/nickl- "GitHub: Repositórios do Nickl-"
[github-foundation]: https://github.com/Respect/Foundation/pull/27/commits "GitHub: Pull request do Nickl- para o Respect/Foudation"
