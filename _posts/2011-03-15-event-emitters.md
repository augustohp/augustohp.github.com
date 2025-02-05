---
layout: post
title: NodeJS Event Emitters
category: NodeJs
---

Há algum tempo venho brincando com [NodeJS](https://nodejs.org/). A
brincadeira começou com uma pesquisa sobre gerenciadores de pacote a um
bom tempo atrás até que cheguei ao [NPM](https://npmjs.org/) que possui
uma arquitetura relativamente boa e extremamente interessante.

Mas não estou aqui pra falar do NPM, e sim do NodeJS. O principal fator
dele é aproveitar todo o conceito de ser assíncrono. Não vou discutir o
quão isso pode ser positivo mas vou mostrar como funciona a parte de
emissão de eventos que vem junto com o NodeJS uma vez que a documentação
não se faz muito clara.

## Porque emitir eventos?

O conceito todo de ser assíncrono é não perder tempo esperando por uma
resposta enquanto você poderia estar processando outras. Quem já fez
alguma chamada *Ajax* tem um exemplo prático em mãos do quão isso pode
ser vantajoso.

Enquanto você desenvolve no NodeJS, você o faz usando *JavaScript* e
deveria utilizar esse conceito assíncrono o quanto você puder; óbvio que
como qualquer técnica ela tem suas utilizações e não deve ser utilizada
de forma leviana. Pegue o conceito, treine e repense nas coisas que você
já fez e que poderiam ter um ganho significativo com essa abordagem.

## Show me the code!

Pela documentação do NodeJS o
[EventEmitter](https://nodejs.org/docs/v0.4.2/api/events.html) pode ser
utilizado da seguinte forma:

```javascript
var Events       = require('events');
var EventEmitter = Events.EventEmitter();

EventEmitter.on('chorar', function(para) {
    console.log("Acabaram de chorar para "+para);
});

EventEmitter.emit('chorar','Mamãe'); // Acabaram de chorar para Mamãe
```

O código acima não é lá muito útil se estivermos usando Orientação a
Objetos e os módulos do NodeJS, útil ele pode até ser, mas prático não.
Então como incorporar isso em uma de nossas classes?

```javascript
var EventEmitter = require('events').EventEmitter();

function Pessoa(nome) {
    this.nome = nome;

    function beliscar(quem) {
        if ( quem instanceof Pessoa )
            quem.emit('chorar', this.nome);
    }
}
Pessoa.prototype = new EventEmitter(); // Herdando o EventEmitter

SeuMadruga = new Pessoa('Seu Madruga');
Kiko       = new Pessoa('Kiko');

Kiko.on('chorar', function(agressor) {
    console.log('Mamããããããããããããããããe!!!! '+agressor+" me beslicou!");
})

SeuMadruga.beliscar(Kiko);
```

Como você pode notar, não requer prática muito menos habilidade. Deixe
sua imaginação brilhar agora - longe de mim, por favor. =P

Qualquer coisa, chore aqui nos comentários =P
