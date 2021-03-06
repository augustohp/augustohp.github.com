---
layout: post
title: Arrays nunca mais
date: 2010-12-06
category: PHP
---

Não vou falar nenhuma novidade, muito menos pregar um conceito
alienígena. Arrays são um câncer dentro de um sistema. Porquê?

-   Não possibilitam validação nem formatação
-   São extremamente genéricos
-   Não servem para documentação (Exprimente usar classes e uma IDE)

## Não possibilitam validação nem formatação

Se você trabalha já com objetos, porquê regredir e começar a usar
arrays? Regredir sim. Veja o exemplo a seguir:

```php
    <?php
    class Arquivo {
        protected $_path;

        public function setPath($s) {
            $this->_path = $s;
        }

        public function getPath() {
            return $this->_path;
        }
    }
    ?>
```

Não sei se você nota a riqueza que utilizar classes lhe proporciona. Mas
logo de cara, sabemos que uma instância da classe *Arquivo* poderá
possuir um atributo contendo o *path* daquele arquivo. Note também que a
maioria das coisas é auto explicativa. Você não precisa ler muito código
para chegar a conclusão que essa classe representa um arquivo e irá
conter informações sobre ele.

Agora se quiséssemos algo parecido mas utilizando array, poderíamos
fazer assim:

```php
    <?php
    $arquivo         = array();
    $arquivo['path'] = "";
    ?>
```

Bem menos código certo? Alguns podem argumentar que usar arrays também é
mais rápido que utilizar objetos **mas garanto a você que a diferença de
performance é extremamente ridícula** (coloco benchmarks aqui mais
tarde).

O problema de utilizar arrays é que você joga fora tudo o que você
determinaria numa classe. As informações que aquele pedaço de memória
variável pode ter e obviamente as possíveis validações. Quem garante que
os outros programadores irão enviar um array bem formatado? Um
comentário dentro do código?! Te garanto que não.

Com o tempo você aprende a se defender com o efeito do "programador
filho-da-puta". Desculpa a agressão, mas a intenção é essa mesma.
Acredite, usuários são um inferno na terra? São. Programadores são
piores!

## Conclusão

Esqueça essa história de que arrays são mais rápidos que objetos. Eles
são? Sim. Essa diferença de performace vai fazer com que sua aplicação
melhore ou que seu usuário note alguma diferença? Não.

Não sacrifique a estabilidade do seu software ou a manutenção dele em
troca de poucos milesegundos. A não ser, claro; que você trabalhe no
Facebook ou no Yahoo, tendo que lidar com milhares de requisições por
segundo.
