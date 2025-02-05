---
layout: post
title: Meu ambiente de trabalho
category: Desenvolvimento
---

Gosto de ter meu fluxo de trabalho otimizado: simples e extremamente produtivo. É uma questão de encontrar a melhor solução e ver se ela resiste ao teste do tempo. Talvez por isso me interesse **bastante** pelo ambiente de trabalho dos outros.

Há algum tempo houveram uma série de posts por parte da comunidade PHP em que cada desenvolvedor descrevia seu ambiente de trabalho em 7 itens. Minha idéia aqui é revisitar isso, sem regras dessa vez.

## Um anel para todos governar

Confesso que minha relação com o [bash][] já sofreu bastante. Pequei e usei o [zsh][] durante um tempo mas no fim, o `bash-complete` funciona como deveria enquanto a experiência com o [zsh][] completando comandos era embaraçosa mais vezes do que eu gostaria.

É o [bash][] que me faz sentir confortável em um sistema operacional. Ele foi o motivo deu ter comprado meu primeiro *MacBook*. Ele é o motivo de simplesmente não me importar se estou no Ubuntu, OSX pou qualquer outro Unix. Ele é o motivo deu esperar tão mais de um teclado que do mouse. 

Aliás, se você se considera um programador e não usa ou sabe utilizar um \*nix muito bem (no bom e velho terminal), faça um bem a humanidade e reconsidere o título. Sério.

## Um anel para […] aprisionar

Como já disse, uso o *OSX* e o *Ubuntu* diariamente. A "cola" que liga os dois e deixa tudo relativamente indiferente pra mim (junto com o [bash][]) é o [Homesick](https://github.com/technicalpickles/homesick). Mantenho meu [castle](https://github.com/augustohp/warwick) com muito carinho, que é exatamente tudo que eu gostaria de ter na minha *home*.

### OSX

Este é um caso de amor **e** ódio. 

Tento manter [uma relação atualizada de amores e ódios com relação ao OSX num Gist](https://gist.github.com/augustohp/4000099), contribua você também!

### Ubuntu

Eu gosto de sistemas operacionais debian-like. A experiência de usar um sistema operacional que não tenta te impedir de fazer as coisas ([e segue um padrão bem estabelecido][debian-posix]) é sempre estimulante. Tentar coisas novas é simples como deveria ser, voltar e não se arrepender é gratificante como "tentar" deveria ser em qualquer atividade.

Apesar de uma mania **foda** de foder com os pacotes e seus respectivos padrões (sim, o pleonasmo se faz necessário), compilar as depedências é algo que estou acostumado então nunca sofro mais que o suficiente.

Buscar informações funciona. Sem conexão com internet. Essas duas orações anteriores matam praticamente qualquer distribuição que você quiser comparar contra uma Debian-like.

## Um anel para todos encontrar

Navegadores. Pra mim é uma questão de se decepcionar o suficiente e trocar. Um loop infinito no qual a iteração atual está com o ~~[**firefox**](https://getfirefox.com)~~ [Google Chrome](http://google.com/crome).

Abrir mão de todas minhas informações pessoais pro Google em troca do genrenciamento de usuários do [Chrome](https://google.com/chrome) é uma mão na roda. Eu só evito dar uma olhada no tráfego de rede da minha máquina, é assustador.

Uso também o [vimperator](https://vimperator.org) mais por causa dos motions. Usar um teclado pode parecer coisa de *hipster*, mas é bem mais produtivo e confortável.

## Minha montanha da perdição

Já usei bastante coisa pra criar/editar/ler código, valem ser citados:

* Zend Studio 5.5 (pré-eclipse)
* Netbeans
* Textmate

O mínimo que eu espero de uma ferramenta do tipo:

* Busca decente. (No arquivo, no diretório do projeto e regex *search*)
* Feedback imediato. Se eu digitar, eu quero ver.
* Respeite (facilmente) as diferentes configurações de cada projeto.
* Sintax highligh decente (é incrível como algumas simplesmente ignoram isso).
* Saia do meu caminho.

Tendo isso em mente, hoje, fico alternando sem nenhuma regra entre dois: vim e sublime.

### Sublime Text

Comecei a usar ele assim que saiu o Textmate 2, e foi uma grata surpresa.

- Abas do chrome: de brinde, todo o gerenciamento de memória.
- CMD+T ou CTRL+P: Era a killer feature do *Textmate*, na minha opinião.
- Plugins: Package Installer, Git (não funciona no 3), Alignment, alguns de sintaxe e pronto.
- Snnipets e Temas compatíveis com os do Textmate.
- O comando `subl`

### Vim

Tirando toda idéia [poser](https://www.wikihow.com/Tell-if-You-Are-a-Metal-Poser) de dizer que uso [vim][], diria que ele é um vício bem vindo. Aprender é uma tarefa constante. Com o [vim][] aprendo muito mais do que eu gostaria, mas todos extremamente gratificantes!

- Os [atalhos de movimentação](https://vimdoc.sourceforge.net/htmldoc/usr_03.html) são **um absurdo de práticos**.
- Disponível em qualquer \*nix.
- Ele **realmente** sai do seu caminho.
- Os [diferentes](https://vimdoc.sourceforge.net/htmldoc/intro.html#Normal) [modos](http://vimdoc.sourceforge.net/htmldoc/insert.html#Insert) são [realmente](http://vimdoc.sourceforge.net/htmldoc/cmdline.html#Command-line) uma [ótima idéia](http://vimdoc.sourceforge.net/htmldoc/visual.html#Visual).
- Rápido que é o diabo.
- [Tim pope](https://github.com/tpope).
- [vim-diff](https://vimdoc.sourceforge.net/htmldoc/diff.html).

Git
---

Depois de começar a usar controle de versões, você simplesmente espera que tudo seja versionado. Com o `git` você descobre que "*tudo*" é muita coisa e agora sim, você quer realmente versionar tudo.

Uso ele pra escrever posts nos blogs, como minha lista de tarefas em vários projetos e não canso de me surpreender com as oportunidades que ele oferece.

É uma das poucas ferramentas que realmente recompensa você pelo tempo que você investiu lendo documentações. Eu sempre me pego buscando na `manpage` de algum comando algo que preciso e acabo lendo um pouco mais do que deveria. Acaba que praticamente todo dia descubro algo novo nelas.

# Vagrant (e Puppet)

Eu não vou negar que levei anos pra me sentir confortável num ambiente em que eu conseguisse desenvolver usando várias versões do PHP. Passei por coleções de scripts shell, por diferentes instalações e configurações de servidores web, diferentes formas de organizar as mais bizarras dependências até chegar no php-bulid e phpenv.

A satisfação durou alguns meses até chegar o [Vagrant][]. Ter uma pequena VM rodando em um ambiente extremamente controlado com baixo uso de memória e muito próximo do ambiente de produção da aplicação é simplesmente imbatível por enquanto. Usar essas VMs diretamente na Amazon? Fritas acompanha senhor?!

Usa o [Puppet][] e ter o mesmo conjunto de instruções gerando seu ambiente de desenvolvimento e o de produção é um brinde bem vindo. Ainda namoro a idéia de ter algumas dezenas de shell-scripts bem escritos, mas pra mim (o puppet, sua sintaxe bizarra e o mundo bizarro de orquestração dele) é tolerável simplesmente por causa das contribuições de módulos já existentes no [Puppet Forge][puppet-forge].

# Conclusão

Espero ter apresentado algo que você possa usar ou se identificar no dia a dia.

Já passei pelo sonho de acreditar em ferramentas mágicas. Hoje aprendi que nós fazemos a mágica com as ferramentas que já existem, como por exemplo as que descrevi acima. Eu realmente não preciso de mais nada (sem contar a *Internet*) além delas pra fazer qualquer coisa.

E você, o que tem usado?

PS: Comente, me manda um [tweet](https://twitter.com/augustohp) com suas ferramentas.
PPS: Não tem onde postar? Use um [gist](https://gist.github.com) e me passe o link. ;)

[zsh]: https://www.zsh.org/
[bash]: https://www.gnu.org/software/bash/
[vagrant]: https://www.vagrantup.com/
[puppet]: https://puppetlabs.com/
[puppet-forge]: https://forge.puppetlabs.com/
[vim]: https://www.vim.org/
[debian-posix]: https://wiki.debian.org/POSIX
