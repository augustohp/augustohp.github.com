---
title: Orientação a Objetos - Tell Don't Ask
category: ood
layout: post
date: 2015-07-31
---

Num [post anterior][1] vimos quanta informação do desenvolvedor os
métodos de acesso escondem, não dos objetos em si mas de como os desenvolvedores
podem usar esses objetos no dia a dia.

Continuando a mesma série de exemplos, vamos ver como unir dado e comportamento
para melhorar a comunicação com nossos usuários (desenvolvedores).

## Dados vs Comportamentos

Nos examplos anteriores, tínhamos um valor de desconto em dinheiro. Um desconto
só é útil se aplicado à alguma coisa, certo? Como nossa empresa fictícia vende livros,
vamos ver como seria usar dar desconto em um livro:

~~~ php
namespace MyApp\Promotion;

$book = new Product('Object Thinking (Developer Reference)', 60.00);
$blackFriday = new Discount\Money(10.00);

$finalPrice = $book->getPrice() - $blackFriday->getValue();
$book->setPrice($finalPrice);
~~~

No exemplo acima temos duas classes representando dois dados diferentes: `desconto`
e `produto`. Veja que o comportamento de cálculo do desconto não esta encapsulado
em nada, vamos resolver isso:

~~~ php
namespace MyApp\Promotion;

class DiscountCalculator
{
    public function applyDiscountOnProduct(
        Discount\Money $discount,
        Product $book
    ) {
        if ($discount->getValue() >= $book->getPrice()) {
            $message = sprintf(
                'Discount (%01.2f) is greater than book price (%01.2f).',
                $discount->getValue(),
                $book->getPrice()
            );
            throw new \UnexpectedValueException($message);
        }

        return $book->getPrice() - $discount->getValue();
    }
}
~~~

Agora temos nosso comportamento agindo em dois dados diferentes. Apesar de ser
um exemplo com classes, nada impede os seus dados de serem um array ou qualquer
outra estrutura de dados (apesar de saber que você prefere objetos 😉).

Vamos ver como fica o uso deles com nossa classe tilanga:

~~~ php
namespace MyApp\Promotion;

$calculator = new DiscountCalculator;
$book = new Product('Object Thinking (Developer Reference)', 60.00);
$guguFriday = new Discount\Money(50.00);

$customerCart = $calculator->applyDiscountOnProduct($guguFriday, $book);
~~~

Repare como *a calculadora* depende sempre dos dois objetos mas principalmente
do desconto, que é quando ela é necessária. Separar dados de comportamento pode
ser útil em alguns casos mas existe um grande poder (de comunicação) em unir ambos,
além de ser um dos fundamentos da Orientação a Objetos:

> Código procedural pega uma informação e toma uma decisão. Código orientado a
> objetos pede que objetos façam coisas.
>
> Alec Sharp

Separando *dado* de *comportamento* você cobra do usuário o conhecimento dos
comportamentos associados ao dado. Toda vez que alguém quiser saber o preço que
algum cliente pagou (ou vai pagar) por algo, ela precisa saber dos descontos e
aplicá-los. Você acha mesmo que elas vão sempre saber disso?!

Papai Noel não existe, nem o coelhinho da páscoa. #prontofalei

## Tell, don't ask

O [Tell, don't ask][tda] basicamente diz que juntando os dois (dado e
comportamento) em uma única classe, o desenvolvedor precisa saber menos e o
código tende a ficar mais conciso (e coeso, como  consequência).

Como ficaria nosso exemplo de desconto em dinheiro usando ele?

~~~ php
namespace Myapp\Promotion\Discount;

class Money
{
    private $amount = 0.00;

    public function __construct($amountToDiscount)
    {
        $this->amount = $amountToDiscount;
    }

    public function calculateProductFinalPrice(Product $product)
    {
        $newPrice = $product->getPrice() - $this->amount;
        if ($newPrice <= 0.00) {
            $message = sprintf(
                'Discount (%01.2f) is greater than book price (%01.2f).',
                $this->amount(),
                $product->getPrice()
            );
            throw new \UnexpectedValueException($message);
        }

        return $newPrice;
    }
}
~~~

Pronto. Jogamos a *calculadora* fora, tiramos o método de acesso pra retornar o
valor do desconto e colocamos o método da calculadora dentro do desconto.

Antes o desenvolvedor precisava saber o que fazer com aquele valor, agora ele
precisa decidir se o que ele precisa é o valor do produto com o desconto aplicado
ou não. É justamente desse fato que sai o nome [do princípio][tda]: antes de
permitir algum usuário de pedir alguma coisa (dado), diga/ofereça a ele as
ações (comportamentos) que ele pode usar naquele objeto (dado+comportamento).

~~~ php
$book = new Product('Object Thinking (Developer Reference)', 60.00);
$blackFriday = new Discount\Money(10.00);

$customerCartValue = $blackFriday->calculateProductFinalPrice($book);
~~~

Pensando sempre em quem vai usar seu código, inclusive você, o código acima é
mais simples e menos propenso aos erros de interpretação no futuro.

Como todo comportamento de desconto está disponível e pronto pra usar, expor o
valor de desconto através de um método de acesso é desnecessário. Esse menor
nível de exposição torna o encapsulamento dos algoritmos melhor e portanto, mais
fáceis de evoluir.

É comum nas discussões de segregar (ou não) *dado* de *comportamento*, o pessoal
a favor da união de ambos citar o argumento [dos modelos anêmicos][anemic-models]
em [DDD][] mas, acho que ninguém precisa ir tão longe pra defender os benefícios
desse princípio.

## Agora queremos descontos em porcentagem!

Agora precisamos aplicar um desconto em porcentagem. Refletindo sobre o
problema, não temos muito a fazer além de criar outra classe de desconto
e mudar ou pouco como o valor final do livro é calculado.

Acho sempre válido você pensar nas soluções por você, se possível envie
elas pra mim depois. Como agora não tenho muita opção, segue minha solução
pro problema:

~~~ php
namespace MyApp\Promotion\Discount;

class Percentage
{
    private $fraction = 0.00;

    public function __construct($percentageToDiscount)
    {
        $value = $percentageToDiscount / 100;
        $this->fraction = (float) $value;
    }

    public function calculateProductFinalPrice(Product $product)
    {
        $discountValue = $product->getPrice() * $this->fraction;
        $newPrice = $product->getPrice() - $discountValue;
        if ($newPrice <= 0.00) {
            $message = sprintf(
                'Discount (%01.2f%%) makes product cost nothing!',
                $this->fraction * 100
            );
            throw new \UnexpectedValueException($message);
        }

        return $newPrice;
    }
}
~~~

Usar o [princípio][tda] força você a imaginar como um objeto vai ser usado
e nas informações que o usuário terá quando for consumir a funcionalidade
da sua classe. Pra resolver isso, eu costumo tentar fazer o [código imitar
uma conversa entre duas pessoas][ddd].

Quando você recebe um desconto, como a pessoa comunica esse desconto a você?

1. Você tem 25% de desconto em qualquer produto.
2. Você só vai pagar 75% do produto.
3. Você vai pagar o valor do produto menos o valor dele multiplicado por 0.25.

Imaginando que as três conversas fossem um código de verdade, eu penso
imediatamente nos códigos abaixo:

~~~ php
namespace MyApp\Promotion;

// 1. Você tem 25% de desconto em qualquer produto.
$blackFriday = new Discount\Percentage(25);

// 2. Você só vai pagar 75% do produto.
$blackFriday = new Discount\Percentage(75);

// 3. Você vai pagar o valor do produto menos o valor dele multiplicado por 0.25.
$blackFriday = new Discount\Percentage(0.25);
~~~

Qualquer um dos três códigos pode funcionar, mas qual é a real expectativa do
desenvolvedor quando for consumir o código existente?
[Deixar implementação próxima da forma como vocês conversam sobre uma
funcionalidade dentro da empresa][ddd] evita diversos problemas. Como na nossa
empresa fictícia nos comunicamos usando o primeiro caso, implementamos ele.

Repare no nome do primeiro argumento: `$percentageToDiscount`. Ele tira toda a
ambiguidade do processo e elimina a necessidade do desenvolvedor precisar ler o
resto da classe. Através de um [código limpo][clean] estamos sempre evitando a ambiguidade
e a dúvida onde pudermos.

As diferenças entre os casos 1 e 2 são a forma como vocês conversam sobre a
funcionalidade. Já no caso 3 a coisa se degringola um pouco: Você expõe a conta
de porcentagem pro cliente, o que pode ser prejudicial no futuro, como no [caso
dos métodos de acesso][1].

## Defendendo a separação de comportamento e dados

Existem alguns vários argumentos a favor de manter os dois separados mas de forma alguma
vou esgotar essa discussão, nem que eu fosse presunçoso o suficiente pra achar
que tenho essa capacidade, então minha intenção é te dar opções (ou novos problemas)
pra ao menos facilitar sua escolha.

O primeiro argumento contra a separação costuma ser o da violação de [SRP][], o
que é ótimo se a pessoa se embasar na questão de responsabilidade. É ótimo porque
a questão de responsabilidade em nada viola a unidade de dado e comportamento.
"Um motivo pra mudar" é o que define "responsabilidade" no [SRP][], se você
fizer um bom trabalho de design você consegue ter ambos. Ninguém disse que ia
ser fácil.

O segundo argumento é chato e costuma tocar objetos que precisam ser mapeados ou
serializados. Nesse caso, você tem uma classe que possui informações além de um
método que retorna o mapamento daquele objeto pra outro. Você pode isolar o
mapeamento em outra classe e sempre que a estrutura de dados mudar, mudar essa
classe-mapa também - resumindo, uma bosta. Você pode usar [Reflection][] e fazer
esse mapeamento com [Inflexão][inflection], é um jeito melhor de resolver esse
determinado problema e tenho certeza que não é o único. Aqui o argumento é chato
porque provavelmente você vai cair nos *trade-off*s: analisar diferentes soluções
e adotar a "menos pior" pro seu caso específico.

Em todos os casos, repare que a opinião pouco importa. Usar o "[Tell, don't ask][tda]"
não precisa violar nenhum outro princípio independente da situação mas te convido
a antes de pensar nos princípios, pensar em quem utilizará o código e se todas
as implicações de negócio estarão tão claras pra eles quanto estão pra você. Esqueça
disso e use todos os princípios, você terá problemas. Não disse que os princípios
são ruins, só disse que eles por si só não resolverão todos os seus problemas.

PS: Se você pensou em usar alguns desses argumentos pra defender [Active Record][ar],
eu tenho um argumento contra você: [SRP][] 😄. Eu sou um filho da puta, to ligado. 😘

## Conclusões

Assim como [o uso inconsicente dos métodos de acesso pode ser ruim][1], separar
*dado* dos seus *comportamentos* também é.

Dar aos usuários do seu código ações a serem feitas em cima de determinados dados,
junto com eles, vai melhorar a comunicação do seu código com eles. É essa melhora
de comunicação que impede os problemas de acontecerem.

Eu não falei quase nada sobre o [TDA][], então vá ler mais a respeito:

* O [Andy Hunt e o Dave Thomas][pp] publicaram um [artigo no IEEE][2] além de
  [outro bem mais detalhado no blog deles][tda]. Eu aconselho bastante a você
  ler eles! Eu podia ter colocado esses links na introdução e não ter escrito
  absolutamente mais nada, mas como eu [peguei feijão e strogonoff hoje][self],
  considerem esses links o strogonoff.
* No [Cunningham & Cunningham Wiki][c2] existe [uma discussão][5] dos dois links
  acima com algumas conclusões. Você já sacou que nenhum dos links que eu ponho
  deveriam ser ignorados por vossa senhoria, certo?!
* O [Martin Fowler][fowler] publicou [no bliki dele][4] um artigo bem preguiçoso
  a respeito do princípio. Se você gosta dele e está com tempo, vá lá ler, se não
  vá procurar alguém errado pelas internets. Com esse link aqui é sério, você
  não via perder nada se não ler.
* A [ThoughtBot][] fez [alguns exemplos em Ruby][6] que são bacanas. Sem bla bla
  bla, só exemplos.

PS: Meu obrigado pro [João][joao], [Nelson][] e [Cobucci][] pelo review a mais um
post. Eles são uns 👼 !

[1]: https://blog.augustopascutti.com/orientação%20a%20objetos/2015/06/25/oo-setters-getters.html
[2]: https://media.pragprog.com/articles/jan_03_enbug.pdf
[tda]: https://web.archive.org/web/20121227021359/pragprog.com:80/articles/tell-dont-ask
[4]: https://martinfowler.com/bliki/TellDontAsk.html
[5]: https://c2.com/cgi/wiki?TellDontAsk
[6]: https://robots.thoughtbot.com/tell-dont-ask
[anemic-models]: https://en.wikipedia.org/wiki/Anemic_domain_model
[clean]: https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882
[ddd]: https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215
[srp]: https://drive.google.com/file/d/0ByOwmqah_nuGNHEtcU5OekdDMkk/view?pli=1 "Uncle Bob: Single Responsability Principle"
[ar]: https://en.wikipedia.org/wiki/Active_record_pattern
[pp]: https://pragprog.com/about
[c2]: https://c2.com/cgi/wiki?WelcomeVisitors
[fowler]: https://martinfowler.com
[joao]: https://github.com/netojoaobatista/
[nelson]: https://twitter.com/nelson_senna
[cobucci]: https://github.com/lcobucci
[thoughtbot]: https://thoughtbot.com/
[reflection]: https://php.net/ReflectionClass
[inflection]: https://en.wikipedia.org/wiki/Inflection
[self]: https://twitter.com/augustohp/status/626032867798351872
