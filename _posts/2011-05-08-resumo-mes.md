---
layout: post
title: Resumo do mês (Abril)
date: 2011-05-08
category: PHP,Resumos
---

Seguindo a idéia dos posts mensais de resumo sobre o que aconteceu no
PHP, segue o resumo do mês de Abril. Mais uma vez ressalto que se
esqueci de alguma coisa podem me avisar pelos comentários ou pelo
@augustohp para que possamos manter isso o mais informativo possível.

## Desenvolvimento do PHP

-   [Planejando a 5.4](https://wiki.php.net/todo/php54): Começou o
    planejamento pro que (idealmente) será a versão 5.4 do PHP. O
    processo todo, apesar de algumas coisas já possuírem patches e
    inclusive estarem no *trunk* ainda são discutíveis, ou seja, não
    necessariamente estarão na nova versão;
-   **Buss do Estado do Desenvolvimento do PHP**: Um pouco de background
    a todos é útil, aqui vai. É relativamente comum ver por aí pessoas
    reclamando da PEAR/PECL pelos mais variados motivos. O que começou
    como mais uma sabatina a PEAR/PECL (ambas possuem a mesma base de
    trabalho, o gerenciador de pacotes) acabou virando uma discussão
    maior e óbvio o assunto de fork do PHP veio a tona. Se você quiser
    se interar um pouco mais do assunto, aqui vai uma lista de posts a
    respeito disso:
    -   [4 reasons Drupal should fork PHP
        (inglês)][1]:
        Bem menos polêmico do que o título sugere, mas foi a partir
        daqui que a coisa evolui;
    -   [Is PHP running out of itches to scratch
        (inglês)][tabini]
        Marco Tabini disserta um pouco em cima da conclusão do post do
        Cal Evans (acima) e (minha opinião) acerta em cheio no assunto;
    -   [A roundhouse kick, or the state of
        PHP](https://till.klampaeckel.de/blog/archives/150-A-roundhouse-kick,-or-the-state-of-PHP.html):
        Um belo resumo para quem não esta acostumado a acompanhar todas
        as disussões existentes. Dá um ótimo background sobre PEAR,
        Drupal, e outros projetos; apesar (obviamente) das opiniões
        pessoais;

## Ferramentas

-   [MySQL
    5.6][3]:
    Finalmente uma versão que não é (quase) só balela. Corre lá e da uma
    olhada no que tem de novo, mas pra mim a mais importante foi a
    adição do checksum na replicação de dados. Enfim, se fosse comentar
    só as novidades dessa versão do MySQL, certeza eu tenho que dariam
    alguns dois ou três posts relativamente grandes.
-   [MySQL Sandbox][ms]: Ta aí uma
    ferramenta que eu não conhecia. Ela nada mais é do que um instalador
    de MySQL que permite que você instale várias instâncias numa mesma
    máquina. Nada que não fosse possível antes, mas é uma ajuda muito
    bem vinda uma vez que as instâncias insaladas por ele são
    gerenciadas por ele mesmo. Agora fica fácil você exprimentar a
    replicação do MySQL.
-   [Behat](https://behat.org/): É uma ferramenta BDD que te ajuda
    escrever testes de uma forma muito mais natural do que Testes
    Uniários. Altamente inspirada no Cocumber do Ruby.
-   [Internet Explorer 10
    (Preview 1)][2]:
    Preview do navegador da Microsoft, seguindo o fluxo de mudanças do
    IE9.
-   [Opera 11](https://www.opera.com): Saiu uma nova versão do
    navegador que era meu navegador de escolha antes do Chrome. Ainda
    vale a olhada e o uso.

## Posts

-   [PEAR channnel
    aggregator][4]:
    Um POST que saiu das brasas da discussão de fork do PHP que citei
    acima. Um canal único para PEAR já facilitaria muito o uso para
    pessoas que não estão acostumadas com a arquitetura de funcionamento
    da PEAR.
-   [Discussão do Mime-Type do PHP
    (inglês)](https://cweiske.de/tagebuch/php-mimetype.htm): Nada muito
    sério, porém um post extreamente interessante.
-   [MAC vs PC
    (inglês)](https://mashable.com/2011/04/23/mac-vs-pc-infographic/):
    Gráfico ressantando as diferenças de gosto de usuários MAC e PC. No
    mínimo interessante.

## Palavras finais

O mês de abril passou e foi coroado pela queda da PSN (alguém lembra de
algo tão sério quanto isso na história da Internet?) e pelas discussões
acerca da PEAR. Pra mim a PSN que se exploda, mas a parte de
gerenciamento de pacotes no PHP muito me interessa.\
A PEAR existe a muito tempo, a maioria dos pacotes são compatíveis com
PHP 4 (o que é horrível) e o uso não é muito claro pra quem não a
conhece. Apesar de ser simples (nada muito diferente de um apt-get, yum)
não se vê a utilização em massa dela. Um centro de distribuição de
pacotes/aplicativos já se provou ridiculamente superior (AppStore) ao
famoso Google-For-It e simplificar o uso dela ou criar algo mais simples
com certeza ajudaria muito o ecossistema do PHP.\
Só quero deixar algo claro: criar um gerenciador de pacotes não é
brincadeira de criança muito menos coisa que se faça em um mês. A versão
nova da PEAR (Pyrus) na minha opinião gerencia dependências melhor do
que qualquer outro gerenciador que eu estudei (Rybu Gems e NPM) e é
extremamente fácil criar um pacote para ser distribuído via PEAR. A
parte chata está sempre em manter um channel da onde isso possa ser
baixado.\
Existiu durante muito tempo em minha cabeça a idéia de que a PEAR
deveria morrer e algo novo surgir. Com o Pyrus (PEAR2) acho isso
extremamente desnecessário, na minha opinião o que falta agora é a
comunidade abraçar o projeto (ele já tem um relacionamento estrito com o
PHP e é muito mais abrangente do que qualquer idéia nova que vá surgir)
e tornar a PEAR 2 uma realidade. Um agregador de canais seria útil? Sem
dúvida, mas tem muita questão de segurança envolvida nisso e uma
implementação a altura do PHP e seu uso é bem mais complexa do que a
grande maioria vêm julgando.\
Pessoal da PEAR e do PHP pode ser chato em relação a isso, pode. Mas
eles não estão errados. Vide PSN.

Concluindo? Quer uma dica? Vai brincar com o MySQL novo e o suporte
nativo a memcached.

[tabini]: https://web.archive.org/web/20121205090627/blog.tabini.ca/2011/04/is-php-running-out-of-itches-to-scratch/
[ms]: https://web.archive.org/web/20230405092001/mysqlsandbox.net/news.html
[1]: https://web.archive.org/web/20211204111256/blog.calevans.com/2011/04/07/four-reasons-why-drupal-should-fork-php/
[2]: https://web.archive.org/web/20121222212147/blogs.msdn.com:80/b/ie/archive/2011/04/12/native-html5-first-ie10-platform-preview-available-for-download.aspx
[3]: https://web.archive.org/web/20121226095652/dev.mysql.com:80/tech-resources/articles/whats-new-in-mysql-5.6.html
[4]: https://web.archive.org/web/20120815012456/blog.stuartherbert.com:80/php/2011/04/09/gathering-requirements-for-a-pear-channel-aggregator/
