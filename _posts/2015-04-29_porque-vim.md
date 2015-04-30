---
layout: post
title: Por que VIM?
date: 2015-04-30
category: Desenvolvimento
---

# Por que VIM?

Já escrevi sobre [meu ambiente][1] de trabalho antes então o fato deu usar [VIM][] não deveria ser novidade. Adoro discutir e observar como cada desenvolvedor trabalha no dia a dia mas odeio o fato de ter que compartilhar o editor que várias pessoas usam só pra demonstrar alguma habilidade - ou a falta dela.

## Eu não escolhi usar VIM, escolhi usar o terminal

> Over 1 year, the average Vim user saves 11 minutes in productivity. However, they lose 27 hours through evangelising Vim to non-users.
>
> -- I Am Devloper [(@iamdevloper)](https://twitter.com/iamdevloper/status/588355053104267264) April 15, 2015.

Acho que a maioria das pessoas que usam [VIM][] só querem exercer algum tipo de superioridade com relação às outras. Acredite em mim quando digo: Você **não** deveria usar [vim][]. Siga com as ferramentas que te fazem produtivo, que saem do seu caminho e que te fazem sentir confortável. Nunca esqueça que você é livre e que as ferramentas que você usa pra produzir software são só ferramentas.

> vim é aquela ferramenta que todo programador quer bancar o fodão diz que usa [#phpexperience](https://twitter.com/hashtag/phpexperience).
>
> -- Valdir Bruxel Junior [(@hagnat)](https://twitter.com/hagnat/status/591981964686708737)

Eu escolhi [VIM][] ao [Emacs][] por preguiça. Ele já estava instalado em todos os servidores e ambientes com que tenho contato. Assistir a animação após executar um *ALT/CMD+TAB* entre o terminal e o [Sublime Text][subl] do [OSX][] me matava (literalmente) de ansiedade e eu já passava a maior parte do tempo no terminal mesmo.

Não estou satisfeito com [VIM][] ainda, mas minhas frustrações são menores que as satisfações que ele me dá.

## Comendo boa comida

> “The heart of Unix philosophy is the idea that the power of a system comes more from the relationships among programs than from the programs themselves.”
>
> -- Rob Pike

Eu já tentei [várias vezes][2] mostrar o poder do terminal pra vários desenvolvedores. Acredito que pra desenvolver bom software é necessário consumir bom software, entender os problemas e as soluções dadas leva tempo e determinação. Quanto mais simples a solução, mais difícil de etendê-la.

Já pensou, por exemplo, em porque o [LAMP][] é popular? Te garanto que os [WAMP][]s da vida vieram depois dessa popularização. Estou longe de entender completamente o porquê, mas consigo compartilhar um pouco da minha visão atual:

- [Linux][] dispensa apresentações. Sério.
- O [Apache HTTPD][httpd] é estável, robusto, eficiente e largamente utilizado. Além de ser extramemente flexível: um ótimo [Proxy][httpd-proxy], possui boas opções de [segurança][httpd-security] e muitos outros plugins embutidos.
- O [MySQL][] é simples e robusto. Você pode confiar nele pro seu blog pessoal, [quase todos os outros blogs do planeta][wordpress], ou [quase todo o conhecimento][wikipedia]. A chance de você usar ele sem nem saber o arquivo de configuração dele é grande.
- A arquitetura [shared nothing][] do [PHP][]: Uma requisição, um novo processo. Sem memória compartilhada. Torna ridiculamente simples o desenvolvimento, a escalabilidade e os hosts compartilhados.

Todos esses caras são grandes softwares, em todos os sentidos. Possuem, no sentido de desenvolvimento, uma grande equipe de contribuidores e muitas linhas de código. Mas possuem outra característica em comum: Fazer uma coisa e fazer bem.

Passar bastante tempo no terminal pode parecer uma penitência, e é por muito tempo. Mas aprender como as pequenas ferramentas podem funcionar juntas é fascinante pra dizer o mínimo. Com o passar do tempo você se sente [com super poderes][crawler]: você gerencia seus *TODOs*, suas contas, stalkeia, conversa e derruba aquele site safado sem sair da shell.

Com o passar do tempo, você passa a identificar melhor o problema que cada algoritmo deve resolver. Quais soluções e problemas existem além de como usar elas e eles de forma melhor. Você não vai deixar de usar o Google, perguntar ou ler. Pelo contrário! Mas te garanto, você vai aproveitar **muito mais** as coisas se tornando um preguiçoso invejável - eu ainda chego lá.

Como desenvolvedor isso afeta diretamente o produto final de seu trabalho.

## Você deveria usar mais a shell

Esqueça aquele lance babaca de dividir seu terminal em várias partes e abrir 73 abas pra se sentir [no Tron][jtnimoy]. Comece a fazer tudo que você puder no seu dia a dia dentro de uma shell. Veja como melhoras seu fluxo de trabalho antes de fazer algo que você não precisa e procure entender o que cada ferramente oferece.

Escolha a ferramenta do mês, o [grep][] por exemplo. Aprenda tudo que puder dele, use-o em tudo que puder mesmo que sem necessidade. Quer ver um log? [Grep][]. Buscar ocorrências de uma classe/método? [Grep][]. Achar um commit? [Grep][]. Saber quantas vezes você usou um comando? [Grep][]. Buscar ajuda? [Grep][]. Continue até sua mulher/marido perguntar de manhã "Quem é essa tal de [Grep][]?".

Você vai encontrar casos em que a ferramenta não é útil. Ótimo! Você sabe pra que não usá-la então só falta achar uma boa (ou um conjunto) que torne aquilo possível. Garanto que ela(s) já existem.

> Mas minha IDE já faz tudo isso!
>
> -- Você. Sendo um babaca.

Sua IDE não vai transformar você num programador melhor, ela é uma ferramenta. Assim como o melhor pincel do mundo, com todas as cores do mundo, não faz de você o melhor pintor do mundo. Enquanto um pintor experiente, com um pincel bosta e poucas cores consegue provar por que ele é o melhor pintor do mundo.

Exerça seu direito de nascença e seja livre de todas as ferramentas. Aprenda a usar as mais básicas e a fazer tudo com elas. Imponha esse limite a você mesmo e ganhe continuamente com ele. O caminho [esta][5] [cheio][6] [de ajuda][7].

PS: Fiz uma palestra sobre tudo isso, se você quiser [ver os slides, eles estão disponíveis][slides].

[slides]: //www.slideshare.net/augustopascutti/porque-vim
[grep]: https://en.wikipedia.org/wiki/Grep
[5]: http://linuxcommand.org/learning_the_shell.php
[6]: http://www.oreilly.com/openbook/debian/book/ch13_01.html
[7]: http://www.amazon.com/Power-Tools-Third-Shelley-Powers/dp/0596003307
[vim]: http://www.vim.org/
[emacs]: https://www.gnu.org/software/emacs/
[subl]: http://www.sublimetext.com/
[osx]: https://www.apple.com/osx/
[1]: http://blog.augustopascutti.com/desenvolvimento/2013/11/06/Meu_ambiente_de_trabalho.html
[2]: http://www.slideshare.net/augustopascutti/logs-36298518
[linux]: https://kernel.org/
[shared nothing]: http://en.wikipedia.org/wiki/Shared_nothing_architecture
[PHP]: https://php.net/
[mysql]: https://www.mysql.com/
[lamp]: https://en.wikipedia.org/wiki/LAMP_%28software_bundle%29
[wamp]: http://www.wampserver.com/en/
[httpd]: https://httpd.apache.org/
[httpd-security]: http://httpd.apache.org/docs/current/howto/auth.html
[httpd-proxy]: http://httpd.apache.org/docs/current/mod/mod_proxy.html
[wordpress]: https://wordpress.com/
[wikipedia]: https://wikipedia.org/
[crawler]: http://blog.augustopascutti.com/hacks/unix/2013/09/02/Crawler-de-json-com-mongo-em-5-min.html
[jtnimoy]: http://jtnimoy.com/blogs/projects/14881671-tron-legacy
