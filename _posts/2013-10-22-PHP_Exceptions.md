---
layout: post
title: Exceptions nativas do PHP
categories: [php, exceptions, oo]
---

O [PHP][] possui [algumas Exceptions][spl_exceptions] embutidas que você pode
(e deveria) usar no seu código. Vamos ver como elas se dividem e casos apropriados
pra algumas delas.

Julgo, antes de mais nada, que você sabe o que são e pra que servem as
[Exceptions][exceptions] e que elas só fazem sentido dentro de um código
[Orientado a Objetos][oo].

# As Exceptions nativas do PHP

Como você poderia esperar, o [PHP][] fornece [exceptions][] pras ocasiões mais
comuns, a hierarquia delas é a seguinte:

* [LogicException][]: [BadFunctionCallException][], [BadMethodCallException][],
[DomainException][], [InvalidArgumentException][], [LengthException][], [OutOfRangeException][].
* [RuntimeException][]: [OutOfBoundsException][], [OverflowException][],
[RangeException][], [UnderflowException][], [UnexpecedValueException][].

## Logic Exceptions

[Conforme o próprio manual do PHP][LogicException], devem se referir à erros que
poderiam ser identificados no momento de compilação do código. Como o [PHP][] é
interpretado temos que dar uma convertida nesse pensamento.

Vamos ver, por exemplo, duas [LogicException][]:

    <?php
    namespace MyApp\DateTime;

    class Weekday
    {
        private $name;

        public function __construct($intDayOfTheWeek)
        {
            $this->name = $this->getNameByNumber($intDayOfTheWeek);
        }

        public function __toString()
        {
            return $this->name;
        }

        private function getNameByNumber($dayOfTheWeek)
        {
            if (false === is_int($dayOfTheWeek)) {
                $exceptionMessage = 'Integer expected.';
                throw new \InvalidArgumentException($exceptionMessage);
            }

            if ($dayOfTheWeek < 0 || $dayOfTheWeek > 6) {
                $exceptionMessage = 'Integer between 0 (zero) and 6 (six) expected.';
                throw new \OutOfRangeException($exceptionMessage);
            }

            return date('l', strtotime("Sunday + ${dayOfTheWeek} DAYS"));
        }
    }

Como o [PHP][] é basicamente uma cola entre diferentes bibliotecas em [C][],
além de ser fracamente e dinamicamente tipado; algumas coisas jamais aconteceriam:
como o exemplo acima produzir um erro no momento de interpretação.

Ao passar alguma coisa diferente de um inteiro pra um método
(que só aceita inteiros), o compilador de uma linguagem tipada deria um erro
(assim como o [InvalidArgumentEception][]) acima.

As demais [Exceptions][] são um "brinde", como a [OutOfRangeException][]!
Sabemos qual o *range* (limite mínimo e máximo) de inteiros, logo podemos lançar
uma [Exception][] (como feito acima) nessas situações.

Um ponto interessante desse grupo de [Exceptions][] é que qualquer uma dentro deste
tipo deve gerar (diretamente) alguma correção no seu código,
[como o próprio manual dita][LogicException].

## Runtime Exceptions

Existem erros e/ou situações que podem ser previstas mas que não deveriam acontecer.
Por definição isso é uma [Exception][]. Mas extrapolando a situação, existem casos
que não podemos controlar em momento de compilação ou na passagem de argumentos, já
que lidamos (na grande maioria dos casos) com informação dinâmica (gravamos e buscamos
informações em Bancos de dados, serviços, etc).

Esse grupo de [Exceptions][] serve pro caso descrito no parágrafo anterior, ou seja:
erros que ocorrem somente na nossa aplicação enquanto ela possui (consome/produz) dados
no ambiente real dela.

Como podemos extender, um caso viável de extensão e criação de uma nova [Exception][]
seria:

    <?php
    namespace MyApp\Exception;

    class RecordNotFound extends \OutOfBoundsException
    {
        // noop.
    }

Sempre que buscarmos um registro, por uma coluna `id` por exemplo, e não encontrarmos;
podemos lançar essa [Exception][]. A [OutOfBoundsException][] pode ser usada sempre que
formos consumir uma chave (de um array, por exemplo) que era deveria existir mas não
existe.

Um outro exemplo de uso pra outra [Exception][] deste grupo seria numa paginação:
sua aplicação (ou algum usuário) tentar acessar uma página que não existe. Lançar uma
[RangeException][] neste caso é viável.

Note que apesar do nome conter *range*, assim como no exemplo do [OutOfRangeException][],
note a diferença da natureza do erro: no caso do [OutOfRangeException][] era possível saber
o que esperar e quais eram os únicos valores válidos. Pra [RangeException][] ocorrer, dependemos
das informações em alguma lugar e do usuário (ou nossa aplicação) utilizar uma página
que não pode ser acessada.


## Perguntas frequentes

> Qual a diferença entre a OutOfRangeException e a OutOfBoundException

Elas são de naturezas (tipos) diferentes:

* Uma depende das informações que sua aplicação consome e produz. ([OutOfBoundException][])
* Outra possui valores bem determinados de limite, que não dependem diretamente de informações produzidas. ([OutOfRangeException][])

Note, porém que a origem da informação não tem relação direta com a [Exception][]
que você deve utilizar. Pensando nos exemplos dados, se ao querer pegar o dia da semana
a partir de um número que é gravado no banco de dados e no banco existe um 9 (nove)
você ainda deve lançar uma [OutOfRangeException][]; mesmo que essa informação tenha sido
produzida e consumida.

Porquê? Porque seu problema foi um problema de validação, um valor inválido não
deveria ter sido produzido em primeira instância. Muito menos ser persistido no
banco de dados. Vá arrumar seu código!

PS: o que não quer dizer que [RuntimeException][]s não devam produzir mudanças no
código.

[php]: https://php.net "PHP: Hipertext Preprocessor"
[spl_exceptions]: https://www.php.net/manual/en/spl.exceptions.php "PHP Manual: SPL Exceptions"
[exceptions]: https://php.net/exceptions "PHP Manual: Exceptions"
[oo]: https://en.wikipedia.org/wiki/Object-oriented_programming "Wikipedia: Object Oriented Programming"
[LogicException]: https://www.php.net/manual/en/class.logicexception.php "PHP Manual: Logic Exception"
[BadFunctionCallException]: https://www.php.net/manual/en/class.badfunctioncallexception.php "PHP Manual: Bad Function Call Exception"
[BadMethodCallException]: https://www.php.net/manual/en/class.badmethodcallexception.php "PHP Manual: Bad Method Call Exception"
[DomainException]: https://www.php.net/manual/en/class.domainexception.php "PHP Manual: Domain Exception"
[InvalidArgumentException]: https://www.php.net/manual/en/class.invalidargumentexception.php "PHP Manual: Invalid Argument Exception"
[LengthException]: https://www.php.net/manual/en/class.lengthexception.php "PHP Manual: Length Exception"
[OutOfRangeException]: https://www.php.net/manual/en/class.outofrangeexception.php "PHP Manual: Out of Range Exception"
[RuntimeException]: https://www.php.net/manual/en/class.runtimeexception.php "PHP Manual: Runtime Exception"
[OutOfBoundsException]: https://www.php.net/manual/en/class.outofboundsexception.php "PHP Manual: Out of Bounds Exception"
[OverflowException]: https://www.php.net/manual/en/class.overflowexception.php "PHP Manual: Overflow Exception"
[RangeException]: https://www.php.net/manual/en/class.rangeexception.php "PHP Manual: Range Exception"
[UnderflowException]: https://www.php.net/manual/en/class.underflowexception.php "PHP Manual: Underflow Exception"
[UnexpecedValueException]: https://www.php.net/manual/en/class.unexpectedvalueexception.php "PHP Manual: Unexpected Value Exception"
[C]: https://en.wikipedia.org/wiki/C_language "Wikipedia: C Language"
