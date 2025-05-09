---
layout: post
title: Controle de Versões
category: Desenvolvimento
published: true
---

Você trabalha com desenvolvimento, seja em equipe ou sozinho, você
precisa de um sistema de controle de versões. É simples assim. Você
precisa e ponto. Fazendo uma analogia a religiões, toda religião que se
preze deveria ter um Deus como o [Monstro Spaguetti
Voador](https://en.wikipedia.org/wiki/Flying_Spaghetti_Monster) assim
como todo desenvolvedor que se preze deveria se apegar a um software de
controle de versões.

Existem diversos deles, o intuito aqui é apresentar os que considero
sendo os dois principais existentes e ajudar você a escolher um deles.

## Controle de Versões 101

Um sistema de controle de versões deve, invariavelmente, manter versões
de seu software. Dã! Pra isso, ele centraliza todo o código em um
**repositório** que é basicamente um banco de dados com todo código da
sua aplicação. Alterações nunca são feitas diretamente no
**repositório**, ele é o altar (ou aterro sanitário) de todo seu código.
As alterações devem ser feitas em cópias locais de trabalho ou as
**working copies** e elas (sim) enviam as mudanças de código para os
**repositórios** através de **commits**.

Funciona basicamente assim: você configura o servidor e cria um
repositório, depois você solicita ao repositório uma cópia daquele
código (**checkout**), essa cópia é sua **working copy**, sua cópia de
trabalho. Você segue destruindo tudo o que um dia foi bonito e
funcional, e assim que se dê por satisfeito, você envia as modificações
para o repositório através de um **commit**. Nenhuma alteração da sua
cópia de trabalho vai para o repositório sem que você efetue o
**commit**.

Todo commit gera uma nova **revisão** do código como um todo. Se você
estiver trabalhando sozinho, o fluxo de trabalho é basicamente este.
Agora, se existerem mais pessoas (ou macacos, ou bestas, ou antas,
mulas, etc ...) a coisa pode ficar mais legal. Como cada commit gera uma
revisão e as revisões não são enviadas automaticamente para todas as
cópias de trabalho (se você alterou algo em que outra pessoa esteja
trabalhando, alguém vai ter de fazer o trabalho de condenado e juntar
essas duas revisões), é necessário que você (e os demais) **atualizem**
suas cópias de trabalho com o código existente no controle de versões.

O **update** (atualização) é basicamente o envio de um **delta** (uma
diferença) pelo repositório para sua cópia de trabalho, essa diferença é
feita com base na revisão que está sua cópia de trabalho com a do
repositório.

O repositório é responsável por manter a integridade do código, portanto
ele não permite que alguém em uma revisão anterior a atual (**head**)
envie alterações (commit). Essa lambança toda pode (e irá) gerar
**conflitos**. Você e o Zezinho estão alterando o mesmo arquivo, se o
Zezinho efetuar o commit antes de você, você terá de fazer um **update**
da sua cópia local para depois enviar seu commit. Como vocês alteraram o
mesmo arquivo, o sistema de controle de versões irá gerar provavelmente
um **diff** entre seu arquivo e o do repositório (que é a revisão do
Zezinho) e através desse diff você irá gerar a versão atual do arquivo
em questão. Eu disse *provavelmente* porque se as diferenças não
estiverem nas mesmas linhas é muito provável que o próprio sistema de
controle de versões resolva o conflito em si.

Resumindo: você faz um **checkout** a partir do repositório para obter
sua **working copy**, faz as alterações que forem necessárias e efetua
um **commit** para gerar uma nova **revision** do código. Simples,
certo? É simples mesmo.

## O que o controle de versões traz a você?

Ele é o histórico de todo seu software. Através dele você consegue saber
quem alterou o que, quando e se a pessoa for minimamente digna, o
porquê. O "porquê" só está disponível para você caso a pessoa que
efetuou o **commit** informe um **log** das alterações que foram
enviadas.

Se você tem um software que roda em vários clientes e você deseja
atualizar o software no cliente; você pode fazer isso pedindo um
**diff** para o **repositório** da revisão do software no cliente para a
revisão que você deseja que o software seja atualizado. Esse diff pode
ser aplicado de diversas maneiras de forma automática no código do
cliente e você será uma pessoa extremamente feliz.

Sabe aqueles blocos de código comentados que volta e meia aparecem?
Então, eles vão para o limbo, uma vez que você não precisa mais ficar
guardando eles. Eles estão sãos e salvos no repositório em alguma
maldita e esquecida revisão.

## Quais os sistemas de controle de versão existentes?

Existem vários. Mesmo. O [PHP](https://php.net) utiliza atualmente o
[SVN](https://subversion.apache.org/), mas antes dele utilizava o
[CVS](https://www.cvshome.org/eng/). Agora, o *buzz* do momento (do
passado, eu diria. Ele já está aí a um bom tempo) é o
[Git](https://git-scm.com/). Eu não pretendo detalhar cada um, até mesmo
porque não cheguei a utilizar todos, mas pelo menos dois que tenho uma
experiência razoável e são software-livre.

Existem outros, como:

-   [Mercurial](https://www.mercurial-scm.org/)
-   [Bazaar](https://en.wikipedia.org/wiki/Bazaar_(software))
-   [Monotone](https://www.monotone.ca/)
-   [Perforce](https://www.perforce.com/)
-   [SourceSafe](https://msdn.microsoft.com/en-us/library/3h0544kx(v=vs.80).aspx)

### Subversion (SVN)

Ele é a evolução do CVS. Evolução por algumas diferenças sutis que no
fim resolvem um grande problema. No SVN um **commit** é atômico (assim
como em praticamente todos os demais sistemas de controle de versões),
ou seja: o commit só acontece caso tudo tenha dado certo. Agora vem a
pergunta: o que pode dar errado? Instabilidade na rede. Você faz seu
commit e sua cópia de trabalho está enviando o delta para o repositório,
sua conexão cai ou um tsunami acaba com tudo; no SVN caso coisas assim
aconteçam, o código no repostírio permanece intacto (coisa que no CVS
não acontecia).

No subversion também, o ato de copiar um diretório de dentro do
repositório é uma operação "barata". Ele não vai duplicar os arquivos,
ele vai simplesmente criar um apontamento para a revisão da onde aquele
diretório saiu e manter os deltas daquele "novo" diretório dali para
frente. Isso é útil quando você precisa "congelar" uma revisão, o que
normalmente acontece quando você tem o *release* do seu software; você
vai lá, copia todo o diretório da sua aplicação e renomeia o diretório
com o nome da versão. Pronto.

O SVN hoje é mantido pela Apache, é um projeto extremamente maduro e uma
infinidade de ferramentas que suportam ele. Diria que ele é praticamente
o sistema de controle de versão padrão de qualquer software que se
integre a um controle de versões. Ele surgiu em 2000 e possui muito
material por aí ensinando e ajudando a utilizá-lo.

### Git

O Git é o menino prodígio atual do grupo. Ele é na minha opinião (e na
de muitos) o melhor existente. Ele foi criado com um propósito simples:
ser utilizado no desenvolvimento do kernel do Linux. Em 2005 um ato
infeliz, interpretado de maneira infeliz e colocado a público por um
idiota fez com que a licença do [BitKeeper](https://www.bitkeeper.com/)
que o kernel utilizava de forma gratuita fosse revogada e como nenhum
sistema de controle de versões existente (livre e comercial) atendeu as
demandas do senhor Linus, ele resolveu desenvolver um. A título de
curiosidade, acho que lembro de todas elas:

-   Manter o código intocado, não importa o que
-   Ser distribuído, a fim de não necessitar de conexão com internet
    para que commits sejam efetuados
-   Ser rápido

Com relação a manter o código "intocável", ele queria que o repositório
fosse resistente a corrupção de dados. Acredite, isso acontece com uma
frequência enorme quando você tem um volume de escrita muito grande em
disco. Pra que haja essa segurança, o Git faz um hash de tudo que entra
e sai dele; se o hash que foi enviado ou que existe agora não é o mesmo
hash da revisão que originou aquilo, algo aconteceu.

A parte de ser distribuído é interessante. Toda cópia local de trabalho
é um repositório também, ou seja; possui todo o código e todas as
revisões existentes. Quando você efetua um commit, você está enviando a
alteração da sua cópia local para um repositório local; e só depois,
através de um **push** você envia suas alterações para outro
repositório, no caso o **origin** (a origem).

Quanto a velocidade, é ridículo comparar o Git ao Subversion. Sem
exagerar, um commit no subversion pode demorar umas 50x mais do que um
no Git dependendo da quantidade de arquivos, e eu estou considerando o
commit e o push no Git.

O Git ainda merece uma menção honrosa com relação a resolução de
conflitos. Ele resolve em praticamente todos os casos os conflitos de
arquivos sozinho. Sinceramente, se algum software algum dia publicar uma
*libnorris*, um dos meus candidatos favoritos a essa façanha é o Git.

A desvantagem em relação ao SVN é a quantidade de suporte disponível por
aí. Apesar de já ser bem grande e rasoável, comparar o suporte ao Git
contra o suporte ao Subversion é mais ou menos como comparar a
velocidade dos dois, só que desta vez o Subversion da um banho no Git.

## Conclusão

Se você já usa ou não um controle de versões, e não usa o Git (o
Mercurial é praticamente um irmão gêmeo dele), dê uma chance a ele, só
esteja preparado para ler um pouco e usar bastante o terminal (acredite,
não é nada doloroso com o Git).

Caso você não seja uma pessoa muito apegada ao terminal, vá de SVN e
seja feliz também.

## Eu já conheço e já uso controle de versões

Ótimo para você. Você conhece
[branching](https://en.wikipedia.org/wiki/Branching_(software)?) Não?! Dê
uma olhada e você será mais feliz ainda.

Dica de amigo: se você for desenvolver utilizando branching, o faça
utilizando um sistema de controle de versões distribuído (Git,
Mercurial, Monotone, Bazaar) porque eles vão fornecer um sistema de
**merge** muito superior e vão poupar sagradas horas a você.
