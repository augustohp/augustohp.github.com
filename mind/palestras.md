lastIndexlestras

Abaixo a lista de palestras, escrevo este parágrafo como promessa de manter esta
lista sempre atualizada.

PS: a quem estou enganando =P

- [DSLs](#melhorando-a-comunicação-de-suas-apis-com-dsl)
- [Por que VIM?](#why-vim)
- [Escalabilidade](#guia-do-mochileiro-para-escalabilidade)
- [Banco de Dados: Você conhece o que você usa?](#bancos-de-dados-voc%C3%AA-conhece-o-que-voc%C3%AA-usa)
- [PHP: The small Things](#php-the-small-things-15min)
- [Somos jardineiros](#somos-jardineiros-25min)
- [Frameworks PHP](#frameworks-php-50min)
- [Integração contínua: Testar é bom, integrar é melhor ainda](#testar-%C3%A9-bom-integrar-%C3%A9-ainda-melhor-50min)
- [TDD: Test Driven Development com PHP](#tdd-test-driven-development-em-php-50min)
- [PHP: Encoding](#encoding-e-o-php-50min)
- [SPL: Standard PHP Library](#spl---standard-php-library-50min)
- [Guia de certificação PHP](#de-sobrinho-a-zce-50min)
- [Aprendendo com o Open Source](#aprendendo-com-o-open-source-50min)
- [Logs: O que eles comem, onde vivem e como se reproduzem](#logs-o-que-eles-comem-onde-vivem-e-como-se-reproduzem)

# Bancos de Dados: Você conhece o que você usa?

Descrição curta: Todos nós temos que usar algum banco de dados relacional em nossas aplicações, mas será que todos nós conhecemos como esses bancos funcionam? Porque criamos índices, relacionamentos e colunas de tipos determinados?

Descrição longa: Pra que serve a SQL que digitamos? Porque criar índices melhora a performance de uma query? O que são prepared statements? Como testar a performance de um banco de dados? Como projetar bem uma banco de dados relacional? Não sabe as respostas pra estas perguntas? Veja essa palestra.

Referências

- [Applied Mathematics for Database Professionals](http://www.amazon.com/Applied-Mathematics-Database-Professionals-Experts/dp/1590597451/ref=sr_1_11?s=books&ie=UTF8&qid=1312492304&sr=1-11)
- [Foundation for Object / Relational Databases: The Third Manifesto](http://www.amazon.com/Foundation-Object-Relational-Databases-Manifesto/dp/0201309785/ref=sr_1_32?s=books&ie=UTF8&qid=1312492351&sr=1-32)
- [Fundamentals of Relational Database Management Systems (Studies in Computational Intelligence)](http://www.amazon.com/Fundamentals-Relational-Management-Computational-Intelligence/dp/364208012X/ref=sr_1_40?s=books&ie=UTF8&qid=1312492382&sr=1-40)
- [How SQL Database Engines Work - Dr. Richard Hipp, creator of SQLite](http://www.youtube.com/watch?v=Z_cX3bzkExE&list=PL7AB44E6784218FD8&index=3=)

# PHP: The small things. (15min)

Descrição curta: Todos nós já usamos um banco de dados relacional em nossas aplicações, mas nós conhecemos como esses bancos funcionam? Porque criamos índices, relacionamentos e colunas de tipos determinados?

Descrição longa: Existem pequenos detalhes no PHP (e em outras linguagens também) que podem fazer grande diferença na entrega de um projeto. Contas que não batem, condições que não fazem sentido, entre outros. 

# Somos jardineiros! (25min ou 50min)

Descrição curta: Acredito sem dificuldade ao ver e escutar de um engenheiro que uma ponte terá tantos metros, tantos pilares e que ela ficará exatamente daquele jeito quando pronta mas me recuso a acreditar em alguém que me diz que um software será entregue exatamente do jeito que foi pedido inicialmente. Eu não sou um engenheiro, sou um jardineiro!

Descrição longa: Mudanças em projetos são sempre inevitáveis. Sempre. Sempre e ponto final. Se você ainda não acredita nisso, mudará de opinião em breve. A questão é que precisamos estar preparados para as mudanças, para riscos inesperados e planos desperdiçados. 
Minha intenção é demonstrar situações comuns e os erros comuns em lidar com cada uma delas.

# Frameworks PHP (50min)

Descrição curta: Dúvidas na hora de escolher um framework PHP? Que tal um panorama entre os principais?! Seus pontos fortes, fracos e como eles podem melhorar sua produtividade!

Descrição longa: Você sabe para quê serve um framework? Em que pontos ele pode te ajudar, onde e quando utilizar um?! E quanto a escolher um framework dentre as dezenas existentes? Saiba quais os pontos que você deve avaliar antes de escolher um framework e como avaliá-los! De brinde veja a avaliação dos principais frameworks existentes em PHP hoje: Zend Framework, CakePHP/Code Igniter/Yii e Symfony.

# Testar é bom, integrar é ainda melhor. (50min)

Descrição curta: Todos nós testamos nossas aplicações de um jeito ou de outro. Mas será que testar só é suficiente? Será que podemos melhorar nossa aplicação e trabalhar menos?

Descrição longa: Testar uma aplicação antes de colocá-la no ar é uma prática tão óbvia quanto respirar para continuar vivendo. Mas talvez você possa aproveitar melhor seu tempo de testes para fazer outras coisas além de só testar. Lógico, testando melhor as coisas. Como? Não é difícil, não dói e nem requer muito aprendizado.

Referências

- [xUnit Test Patterns: Refactoring Test Code (Gerard Meszaros)](http://www.amazon.com/xUnit-Test-Patterns-Refactoring-Code/dp/0131495054/ref=sr_1_1?s=books&ie=UTF8&qid=1316721412&sr=1-1)
- [Patterns of Enterprise Application Architecture (Martin Fowler)](http://www.amazon.com/Patterns-Enterprise-Application-Architecture-Martin/dp/0321127420/ref=pd_sim_b9)
- [Test Driven Development: By Example (Kent Beck)](http://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530/ref=sr_1_5?s=books&ie=UTF8&qid=1316721412&sr=1-5)

# TDD: Test Driven Development em PHP (50min)

Sessão quase-interativa de TDD acompanhada de um repositório GIT contendo todo o código gerado na palestra.

Links

- [Repositório no GitHub](http://git.io/tdd): Código gerado para palestra e apresentado na mesma. Veja os commits ;)

# Encoding e o PHP (50min)

Descrição curta: Você sabe o que é encoding? Os problemas que eles implicam? Caso não saiba, pare de chutar o encoding de suas páginas ou aplicação e assista a essa palestra.

Descrição longa: Apresentados problemas do PHP com carecteres multi-byte e as possíveis soluções atuais da linguagem (PHP < 5.3 ): iconv e mbstring.

# SPL - Standard PHP Library (50min)

Descrição curta: A partir da versão 5, o PHP vêm adicionando funcionalidades necessárias a todos os desevolvedores dentro da própria linguagem, através da SPL. Saiba como ela pode facilitar sua vida.

Descrição longa: Introdução a Standard PHP Library através de exemplos e uma breve introdução à Orientação a Objetos do PHP 5. São demonstrados Iterators, RecursiveIteradors, DirectoryIterators, ArrayIterators, ArrayAccess, Exceptions e Auto Load.

# De sobrinho a ZCE (50min)

Descrição curta: Qual o caminho de um desenvolvedor PHP. Srá que existe um patamar em que não há mais para onde ir? Quais as diferenças entre um sobrinho e um profissional, como você pode trilhar seu caminho de sucesso dentro do mercado e da comunidade.

Descrição longa: Existe uma diferença entre desenvolvimento amador e profissional. Ambos geram resultado, ambos funcionam; mas funcionar é realmente o que deve servir de base de qualidade para seu projeto?
Mudar é bom, evoluir é necessário. Como acompanhar a evolução das coisas e sempre se manter na crista onda.

# Aprendendo com o Open Source (50min)

Descrição curta: Será que o código aberto nos dá **só** a liberdade de modificar o software ou **muito mais**?

Descrição longa: Você pode estar perdendo muito mais do que imagina, ignorando as práticas e padrões utilizados na grande maioria de projetos Open Source. Quais os benefícios e lições que você pode aprender com esses projetos?
Quais os erros, acertos e como um projeto onde ninguém recebe nenhum valor monetário para contribuir é na grande maioria das vezes um produto muito melhor do que os gerados por pessoas que são pagas para fazer aquilo.

# Logs: O que eles comem, onde vivem e como se reproduzem.

Como utilizar os arquivos de log (servidor web, PHP) e como gerá-los.
Quais as configurações que afetam o comportamento da geração de log
no PHP, como gerar mensagens melhores e arquiteturas comuns para manter
e utilizar melhor o pontencial dessas mensagens.

[Slides v1](http://www.slideshare.net/augustopascutti/erros-22750749)
[Slides v2](http://www.slideshare.net/augustopascutti/logs-36298518)

## Referências

- [Livro] The Cathedral and The Bazaar (Eric Raymond)
- [Livro] The Mythical Man Month (Fred Brooks)
- [Livro] The Design of Design (Fred Brooks)
- [Livro] Domain Driven Design (Eric Evans)
- [Livro] Refactoring - Improving Existing Code (Vários Autores)

---------

# Escalando aplicações PHP

Quais problemas você pode enfrentar e quais arquiteturas vão lhe ajudar a criar (e manter) soluções que atendam o crescimento da sua aplicação.

# Why VIM?

How to design things using limitations as a feature? 

We grew lazy on tools come bundled with features ready to be used and forgot what lies behind them. By limiting yourself more and more to the terminal you can learn how to design better solutions which interact well with others.

This is not a talk about an editor, it is to inspire and show you can much good (and free) stuff you are missing for not using the terminal you probably complain to use when needed.

- [Slides already presented](http://www.slideshare.net/augustopascutti/porque-vim).
- [Past evaluations from people who saw it](https://joind.in/event/php-experience-2015/por-que-vim-por-que-decidi-trocar-uma-ide-por-um-editor-no-terminal).
- [A post explaining the talk](http://blog.augustopascutti.com/desenvolvimento/2015/04/30/porque-vim.html).
- [Video](https://www.youtube.com/watch?v=Z_XJys9qyGk)

# Guia do mochileiro para escalabilidade

Escalabilidade em um sistema é planejada desde a sua concepção ou as consequências deverão ser aceitas. Como entender a arquitetura de uma aplicação web, como usar essa arquitetura a seu favor e quais são as práticas mais comuns será o conteúdo dessa palestra. Nada de teoria, você leva pra casa um conjunto de VMs pra experimentar e aprender o que foi apresentado.

- [Slides](http://www.slideshare.net/augustopascutti/mochileiro-escalabilidade).
- [Open repository with multi Vagrant VMs](https://github.com/augustohp/palestra-escalabilidade).
- People comments on previous talks:
  - [PHPEste 2015](https://joind.in/event/phpeste/guia-do-mochileiro-para-escalabilidade).
  - [PHP Conference Brasil 2013](https://joind.in/event/php-conference-brazil-2013/guia-do-mochileiro-para-escalabilidade)

# Melhorando a comunicação de suas APIs com DSL

Como criar DSLs com PHP (internas e externas) através de dois exemplos práticos. Porque e quando DSLs são úteis e como introduzí-las no seu dia a dia.

* [Video](https://www.youtube.com/watch?v=LzwtXNyg9vE)
* [Post](https://gist.github.com/augustohp/5a271ec30335f2aec252)
* [Slides](http://www.slideshare.net/augustopascutti/melhorando-sua-api-com-dsls)
* [Avaliações](https://joind.in/event/php-experience-2016/melhorando-a-comunicao-da-api-atravs-de-dsl)


---------

# Sobre Augusto Pascutti

Descrição curta: ZCE, Co-fundador PHPSP, desenvolvedor, jardineiro e envagelista do XKCD.
Developer for 10+ years. Fan of open source, developer groups (co-founded PHPSP), Randal Munroe and PHP.

Descrição longa: Augusto Pascutti é desenvolvedor PHP com 6 anos de experiência, trabalhou em projetos Open Source como CakePHP, Zend Framework e Habari. É evangelista PHP e de boas práticas, Zend Certified Engineer para PHP 5, fundador/coordenador do PHPSP e host do PHPSPCast.

# Links

- [Slides de palestras já ministradas](http://www.slideshare.net/augustopascutti)
- [Avaliações de pessoas que viram a palestra](https://joind.in/user/view/943)
- [Perfis Sociais](http://about.me/augustohp): Meus perfis em diversas redes sociais
- [Perfil do GitHub](http://github.com/augustohp): Meus códigos Open Source
- [Blog Pessoal](http://augustopascutti.com): Quando tem mais texto que código
- [PHPSP](www.phpsp.org.br): Grupo de desenvolvedores PHP do Estado de São Paulo
