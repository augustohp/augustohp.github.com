---
layout: post
title: Resumo do mês (Março)
date: 2011-04-02
category: PHP,Resumos
---

A idéia de um post por semana é tentadora na teoria, na prática ela é
mais como um martírio. Ainda mais na sexta-feira. O que acontece é que
eu me vi guardando coisas pra poder publicar aqui e acabei por não
escrever os posts, o que fazer então? Resumo do mês! O casamento
(perfeito, espero.) entre a teoria e a prática.

## Desenvolvimento do PHP

-   [Versão
    5.3.6](https://www.php.net/archive/2011.php#id2011-03-17-1): Nova
    versão do PHP! Mais de 60 bugs corrigidos, atualização do SQLite e
    da PCRE. Mais uma vez, é válido reforçar que a árvore 5.2.x não vai
    receber mais muito amor e carinho da parte de ninguém. Estamos todos
    apaixonados pelo 5.3, então corre lá e se atualize.
-   [Invasão no
    PHP.net](https://www.php.net/archive/2011.php#id2011-03-19-2): Algum
    engraçadinho se aproveitou do sistema de wiki do PHP (que não recebe
    muito carinho e manutenção desde que o Lukas Smith se focou no
    Symfony2) mas não houveram danos consideráveis, tirando o fato que o
    Wiki agora está fora do ar =(
-   [Servidor HTTP do PHP](https://wiki.php.net/rfc/builtinwebserver):
    Existe já um patch para o CLI (command line interpreter) do PHP para
    que o mesmo se torne um simples servidor HTTP. Vantagens disso?
    Desenvolvimento sem precisar de Apache, ou qualquer outro servidor.
    O intuito é ter um servidor simples que consiga servir nosso código
    PHP como o Apache serviria, mas sem a necessidade de configurá-lo.
    "Simples" é um termo um tanto um quanto modesto já que o servidor
    HTTP em questão é o mesmo utilizado pelo [NodeJS](https://nodejs.org)
    e portanto algo bem competente.
-   [Tainted data, a revanche](https://wiki.php.net/rfc/taint): Isso é
    relativamente antigo, mas a idéia veio a tona mais uma vez esse mês.
    O conceito da coisa é ligado com segurança de dados. Todo dado vindo
    de globais (POST, GET, etc) vai ser tratado como um risco em
    potencial até que se aplique um filtro nelas. Notices seriam
    acionados toda vez que um dado for usado sem filtro. A idéia é boa e
    a discussão também. Não chega a ter a polemica das Namespaces, mas é
    sempre engraçado acompanhar esse tipo de discussão.

## Ferramentas

-   [Patrocinando o
    xDebug](https://derickrethans.nl/sponsoring-xdebug.html): xDebug é
    uma ferramenta de valor inestimável no desenvolvimento do PHP. Não
    vou mentir que dou uns *var\_dump()* aqui e lá, mas quando preciso
    ver o que está acontecendo de errado mesmo não tem nada que ajude
    mais do que o xDebug. Ele é open source e o Derick põe muito esforço
    no desenvolvimento do mesmo. Ajude como puder no projeto, sugerindo,
    enviado bugs ou até mesmo mandando uma motivação através de uma
    doação em dinheiro.
-   [Validação com
    Respeito](https://www.phparch.com/2011/03/more-powerful-validation-from-respect/):
    Mais um filho brasileiro que saiu na PHP Architect esse mês. Essa
    biblioteca de validação realmente é uma mão na roda. Dê uma olhada
    nos exemplos do artigo e você vai entender o que ela pode fazer por
    você. Essa biblioteca está em desenvolvimento constante e foi/é
    feita pelo grande [Alexandre Gaigalas][6].
-   [Zend Framework
    1.11.4][4]: Versão de
    manutenção da versão 1.11, que provavelmente é uma das últimas da
    série 1.x.
-   [Versão 4 do Horde](https://pear.horde.org/): Você lembra dele?
    Depois de 3 anos em desenvolvimento a equipe de desenvolvimento
    decidiu que [era hora de jogar o filho no
    mundo](https://janschneider.de/news/35/332) e ver como ele se
    comporta.
-   [Anunciando o Aura
    (Solar2)](https://paul-m-jones.com/archives/1738): Começou o
    desenvolvimento da nova versão do Solar. O framework é novo mas vem
    se estabelecendo rápido e ganhando muito respeito. Pelo andar da
    carruagem, eu me arrisco a dizer que ele merece entrar pro grupo
    (até então) só dominado pelo Zend Framework e Symfony ao usar tudo
    que o PHP 5.3 oferece e de um jeito decente. Vamos ver se o pessoal
    mantém o ritmo!
-   [Sublime Text 2](https://www.sublimetext.com/2): Eu não sou um
    grande fã de IDEs. Julgo elas um mal necessário, mas na grande
    maioria das vezes uso um editor de textos um pouco mais turbinado e
    tenho meus problemas resolvidos rapidamente sem estupro da memória
    ram. Pra isso uso (pra quase tudo quase) o
    [Textmate](https://macromates.com), mas apareceu esse carinha como
    quem não quer nada e me agradou muito. Se você também gosta de
    soluções simples, elegantes e leves, dê uma exprimentada.
-   [Firefox 4](https://www.getfirefox.com/): Saiu a versão 4 do
    Firefox. Fazia tempo que o Firefox não me agradava tanto, vale a
    pena baixar.

## Posts

-   **PHP Architect**: É a (praticamente) única revista especializada em
    PHP que existe (em inglês), até um ano atrás ela possuía versões
    impressas, agora é só virtual. Mas o interessante é um membro da
    comunidade brasileira teve um artigo publicado na edição do mês de
    março, nosso membro de peso (sem duplo sentido, ou com. Quem sabe?)
    [Rafael Dohms][3]. Eu não posso reproduzir o
    conteúdo da revista, mas se você entende um pouco de inglês, ela
    vale a assinatura.
-   [Micro otimizações][7]:
    O post está em inglês, só menciono ele aqui porque ele é um grande
    candidato a post ridículo do ano. Pela enésima vez consecutiva. Esse
    tipo de otimização não gera benefício algum pra aplicação alguma. Se
    você usa uma linguagem interpretada e está preocupado com esse tipo
    de ganho, sugiro você a procurar linguagens compiladas e de nível
    mais baixo porquê você está fazendo errado meu caro amigo.
-   [Paralelismo em
    PHP](https://www.d-mueller.de/blog/parallel-processing-in-php/):
    Post interessante para quem não conhece \*nix e os meios que podemos
    utilizar para abrir processos paralelos no PHP. Isso é útil em
    diversos casos que precisamos de muito tempo e processamento e não
    queremos que o usuário sofra com isso. Me lembrou de uma biblioteca
    que eu comecei a fazer e nunca terminei para criar forks usando
    cUrl, quem sabe eu termino e jogo ela no GitHub depois dessa!?
-   [Análise de Performance (Profilling)[5]:
    Um ótimo post sobre como você pode fazer o profilling das suas
    aplicações com as ferramentas mais famosas para tal. Se você nunca
    fez profilling do seu código, corra lá, dê uma lida e experimente. O
    gargalo está sempre onde você menos espera.
-   [Como contribuir com o
    ZF2](https://web.archive.org/web/20200813173110/https://mwop.net/blog/255-How-to-Contribute-to-ZF2.html):
    Deseja contribuir com algum projeto Open Source e não sabe qual nem
    como? Ajude o Zend Framework 2 a sair do forno. O desenvolvimento
    dessa versão já está bem avançado, mas contribuir é muito mais fácil
    do que você imagina. Veja como neste post.
-   [Invasão no
    PHPFog][2]:
    O PHPFog atraiu muita atenção por ser um serviço de cloud voltado
    para o PHP. Se ele vai se dar tão bem quanto o
    [Heroku](https://heroku.com/) ainda é cedo demais para dizer, mas a
    postura da equipe diante de um problema tão sério quanto eles
    sofreram inspirou muita confiança na comunidade como um todo.
    Exemplo de como deve ser a postura das empresas diante de problemas
    críticos.
-   [Parabéns a comunidade][1]: O
    Fernando Camacho escreveu um post parabenizando a comunidade PHP.
    Kudos para todos por sermos uma das maiores e melhores comunidades
    do mundo nerd existente!

PS: Eu não queria comentar nada ... mas tem algum Podcast virando a
esquina logo mais.

[1]: https://web.archive.org/web/20120212065912/phpsp.org.br:80/2011/03/parabens-a-comunidade/
[2]: https://web.archive.org/web/20121015231817/blog.phpfog.com/2011/03/22/how-we-got-owned-by-a-few-teenagers-and-why-it-will-never-happen-again/
[3]: https://web.archive.org/web/20121106162819/www.rafaeldohms.com.br:80/
[4]: https://web.archive.org/web/20130111015326/framework.zend.com:80/changelog/1.11.4/
[5]: https://web.archive.org/web/20110619080238/erichogue.ca:80/2011/03/30/profiling-a-php-application/
[6]: https://web.archive.org/web/20130104155834/gaigalas.net:80/
[7]: https://web.archive.org/web/20150214061025/www.xpertdeveloper.com:80/2010/10/php-coding-tips-for-performance-improvement/