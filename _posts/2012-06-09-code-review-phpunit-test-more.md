---
layout: post
title: Code Review - PHPUnit TestMore
date: 2012-06-11
published: true
---

A idéia aqui é fazer uma revisão de um pequeno componente que achei alguns
meses atrás, que me fez aprender uma coisa (maldosa, diga-se de passagem) que 
definitivamente nem imaginava ser possível com PHP.

O componente na verdade é uma série de funções que nada mais são que atalhos
para os métodos de asserção existentes na classe ```PHPUnit_Framework_TestCase```.
Resumindo: ao invés de chamar ```$this->assertTrue()``` você pode usar ```ok()```
e ter o mesmo resultado.

Estrutura
---------

O [componente](https://github.com/c9s/PHPUnit_TestMore) é de autoria de um chinês: 
**[c9s](https://github.com/c9s)** (o cara é uma *firehose* de projetos). 
Não existem classes, portanto sem maiores problemas com relação à [PSR #0](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md). O componente é um único arquivo com a
declaração das funções e só. Uma suite simples de testes (a cobertura é bem pequena)
também pode ser encontrada no repositório, o que não é  lá um grande problema já 
que todas as funções funcionam basicamente da mesma forma.

Instalação
----------

Não poderia ser mais simples: copie o arquivo contendo as funções, e inclua ele
no bootstrap utilizado pelo PHPUnit.

Em teoria ele deve funcionar em qualquer versão do PHPUnit, posterior à remoção
das funções que ele possuía (algumas possuem o mesmo nome) que foram removidas
sei lá em qual versão =P.

Review
------

A revisão deste código deve ser bem simples e direta, vamos examinar por enquanto
o [arquivo que declara as funções](https://github.com/c9s/PHPUnit_TestMore/blob/master/src/PHPUnit/TestMore.php) 
que serão utilizadas.


<pre class="line-numbers"><code>
    if( ! defined('DEBUG_BACKTRACE_PROVIDE_OBJECT') )
        define( 'DEBUG_BACKTRACE_PROVIDE_OBJECT' , true );
</code></pre>

A constante ```DEBUG_BACKTRACE_PROVIDE_OBJECT``` passou a existir somente na 
versão 5.3.6 quando a assinatura da função [debug_backtrace()](http://www.php.net/manual/pt_BR/function.debug-backtrace.php)
sofreu alteração.

O que está sendo feito é a declaração da constante a fim de que ela exista e se
tenha o mesmo resultado da chamada de função em todas as versões. Uma olhadinha
na documentação do PHP pode resolver dúvidas em relação à isso.

<pre class="line-numbers"><code>
    function ok( $v , $msg = null )
    {
        $stacks = debug_backtrace( DEBUG_BACKTRACE_PROVIDE_OBJECT ); 
        $testobj = $stacks[1]['object'];
        $testobj->assertTrue( $v ? true : false , $msg );
        return $v ? true : false;
    }
</code></pre>

Aí temos a primeira função, que obrigatoriamente recebe um argumento. A assinatura
da função é a mesma do método que ela utiliza, por motivos óbvios isso já é extremamente
interessante.

A primeira coisa que a função faz é retornar o *[backtrace](http://wikipedia.org/wiki/Backtrace)* 
da aplicação COM as instâncias de objetos reais que foram utilizadas. Isso significa
que você pode reutilizar os objetos que foram utilizados para chegar até aquele
momento.

Depois de ter o *backtrace*, a idéia é conseguir utilizar os métodos de asserção
do próprio PHPUnit, da própria suite de testes onde a função é chamada. Isso obviamente
está sempre no mesmo índice do *backtrace*: o primeiro índice posterior à execução
da função.

Sabendo disso, no índice 1 (um) do *backtrace* está a instância do objeto que é
o *TestCase* onde a função foi chamada, ele salva uma referência à este objeto na variável
```$testObj``` e faz a chamada de asserção que ele deseja.

<pre class="line-numbers"><code>
    function dump($e)
    {
        var_dump($e);
        ob_flush();
    }
</code></pre>

Menção den honra à última função: ```dump()```. Ela tem uma utilidade sim dentro
da suite de testes, já que o PHPUnit gerencia o *[Output Buffer](http://www.php.net/manual/en/book.outcontrol.php)* 
para conseguir imprimir o formato desejado do resultado da execução dos testes, 
seja ele: os famigerados pontos (.), o [TestDox](https://en.wikipedia.org/wiki/TestDox) 
ou qualquer outro desejado.

A função [ob_flush()](http://php.net/ob_flush) envia para o output o conteúdo 
do buffer que está sendo controlado, logo vemos output do [var_dump()](http://php.net/var_dump)
como esperado.

Considerações
-------------

Existem obviamente outras formas de se fazer a mágica de consumir métodos de instâncias
já existentes:

<pre class="line-numbers"><code>
    function ok(PHPUnit_Framework_TestCase $testobj, $v , $msg = null)
    {
        $testobj->assertTrue( $v ? true : false , $msg );
        return $v ? true : false;
    }
</code></pre>

Na forma acima, sempre temos que passar a instância do *TestCase* na chamada da
função, o que é um pouco menos elegante do que a solução anterior mas muito mais
simples de se obter e sem a magia negre de reutilizar um objeto do *backtrace*.

Utilizar objetos diretamente do *backtrace* é perigoso por diversos motivos, mas 
o maior problema (na minha humilde opinião, obviamente) é quebrar o fluxo natural
da aplicação. Esse tipo de comportamento não é natural ao programador, é algo que
dificilmente é identificado facilmente (a não ser que você leia realmente o corpo
da função) além de ter um comportamento bem pouco previsível.

O caso acima é um caso à parte:

* A função só funciona se chamada dentro de uma suite de testes
* O código nunca é executado em produção (só nos testes)
* A implementação é bem pequena e inofenciva do ponto de vista de domínios

Enfim, espero que tenha curtido minha primeira revisão pública de código. Não deixe
de criticar ou deixar seu comentário!