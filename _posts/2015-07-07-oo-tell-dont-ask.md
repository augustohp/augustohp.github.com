---
layout: post
title: Orientação a Objetos - Um caso contra os métodos de acesso
category: Orientação a Objetos
---

Quanto de suas classes são compostas por métodos para definir e retornar valores
guardados nela? Você já questionou o benefício da orientação a objetos enquanto
estava criando uma classe? Talvez seja hora de reavaliar nosso conhecimento.

A ideia de um objeto é encapsular uma computação e isso envolve esconder algumas
coisas do usuário. Um método de acesso (ou setter/getter) é uma exposição:

    <?php

    namespace MyApp\Promotion;

    class Discount
    {
        private $value = 0.00;

        public function setValue($float)
        {
            $this->value = $float;
        }

        public function getValue()
        {
            return $this->value;
        }
    }

A proposta de encapsular as coisas é permitir que elas evoluam (ou mudem) sem o
conhecimento do usuário, que no caso é o desenvolvedor. Todo método público
é como uma mensagem de um desenvolvedor pra outro, uma mensagem dizendo
"ei, me use".

Cabe ao usuário decidir se ele quer usar ou não as ferramentas dadas a ele
e na orientação a objetos, para usar um método precisamos das instâncias:


    <?php

    namespace MyApp\Promotion;

    $blackFriday = new Discount;
    $askingToGetFired = new Discount;

Existem casos em que você quer [garantir só uma instância de determinada
classe][singleton] (o que não acho muito válido pro PHP), mas no caso do
nosso desconto queremos obviamente vários tipos de desconto.

No caso de várias instâncias, o que diferencia uma da outra como no exemplo
acima? Quais dos métodos um usuário pode ou não usar e em quais circunstâncias?

Qual a vantagem do código da classe usando os métodos de acesso (get/set)
ao invés de definir o atributo como público?

## Objetos sempre válidos

Nosso trabalho é fazer com que as coisas funcionem 100% do tempo. Deixar
informações implícitas e quebrar promessas (um método é uma promessa) é
a receita para nunca atingir o 100% desejado.

A promessa a ser quebrada aí é a chamada pro `getValue`:

    <?php

    $blackFriday = new Discount;
    $blackFriday->getValue();

Sem valor nenhum de desconto como você poderia querer cumprir essa promessa?
Existem formas de melhorar a comunicação entre nossos objetos, impedindo que
coisas inesperadas aconteçam e que um desenvolvedor precise ler inúmeras linhas
de código pra descobrir como alguma coisa funciona.

A Orientação a Objetos oferece duas mecânicas que consigo pensar em usar nesse
momento. Uma é lançar uma exceção caso nenhum valor de desconto tenha sido definido
e a outra é obrigar um valor de desconto no construtor:

    <?php

    namespace MyApp\Promotion;

    class Discount
    {
        private $value = 0.00;

        public function __construct($value)
        {
            $this->value = (float) $value;
        }

        public function getValue()
        {
            return $this->value;
        }
    }

Existem várias outras maneiras de resolver esse problema. Não usei a exceção
porque um valor de desconto sempre é necessário. Eu poderia criar um validador
de descontos também, mas por enquanto esse tipo de burocracia parece bastante
desnecessário. O melhor código é aquele que não existe.

Criar um código pensando no seu consumo implica em querer contar uma história.
A última coisa que queremos é suspense ou mistério, o melhor tipo de código
é aquele filme de ação tapa na cara, MacGyver:

    <?php

    namespace MyApp\Promotion;

    $blackFriday = new Discount(10);
    $guguSunday = new Discount(25);

Parece que nosso código está fazendo um pouco mais de sentido agora. Repare
que ao ler você sabe que o `Discount` é membro de `MyApp\Promotion` e que
temos dois descontos com valores diferentes. Pare por 1 minuto e pense o
quanto de informação você tem com o código acima que estava escondida por
causa dos métodos de acesso.

Faça o exercício mental de imaginar esse código num caso mirabolante de
checkout num e-commerce. Se você tem uma instância, você pressupõe que ela
faça tudo que ela promete, então se atente a criar uma classe que obriga
todas as instâncias dela a serem válidas. Se você quiser se gabar entre
seus amiguinhos, [você pode até dar um nome bacana pra esse princípio
de design][pola].

Repare também como o consumo da classe utilizando o construtor [conta uma
história][3]. Será que na história contada você tem todas as informações
que precisa pra colaborar ou mudar essa história?

Essa é a pergunta que você deve fazer ao escrever **cada linha de código**.

## Contando uma história completa

Se a nossa empresa agora quiser dar dois descontos: um de 25% e outro de R$15.
Como você vai instanciar as classes de desconto?

Afinal, nossos descontos até agora são em porcentagem ou são valores monetários?

Esse tipo de suspense ou informação que só é óbvia pra quem está criando o código
é o tipo de problema chato. Difícil resolver ele sozinho sem muita experiência e
sensibilidade. A melhor prática pra identificar esses problemas, na minha opinião,
é o [code review][]. Além de alinhar as práticas do time, é imperativo que quem leia
o código entenda ele plenamente.

Outra forma de resolver isso é utilizar comentários mas, eu aprendi que o destino de
um comentário é ser ignorado ou ficar desatualizado. então como a gente resolve
nosso problema sem comentários?

    <?php

    namespace MyApp\Promotion\Discount;

    class Money
    {
        private $amount = 0.00;

        public function __construct($amountToDiscount)
        {
            $this->amount = $amountToDiscount;
        }

        public function getValue()
        {
            return $this->amount;
        }
    }

Podíamos ter resolvido isso de várias formas, imediatamente penso em duas:

- Mudar o atributo de `$value` para `$amountOfMoney`.
- Mudar o nome da classe de `Discount` pra `MoneyDiscount`.

Eu poderia ter [usando as variáveis e atributos pra explicar o que eles devem
conter][explain-variables], mas além disso criei uma *namespace* intermediária
pra deixar claro que iremos precisar de outros tipos de desconto.

O [João Batista Neto][joao] argumentou que obrigar os demais desenvolvedores a
olhar um atributo pra descobrir o que ele é quebra a regra de encapsulamento.
Por isso optei por expressa isso no nome da classe e no argumento do construtor.
Quebrando encapsulamento ou não, o argumento do construtor sempre irá tanger o
escopo de fora da classe e a interno, agradando tanto a mim e [ao João][joao].

## Pensamentos do fim do post

Quero que você pense no seu código e veja quanto dos seus métodos de acesso
fazem alguma coisa de fato. Será que deixar todos os atributos de suas classes
públicos implica no mesmo comportamento do que ter os métodos de acesso? Se sim,
evite-os.

Seus métodos deveriam sempre expressar uma ação e um objeto deve sempre ser válido.
Pense nos métodos públicos como promessas e na responsabilidade de manter várias
promessas desnecessariamente.

Uma boa classe, além de sempre fornecer instâncias válidas, sempre cumpre o que
promete.

## Comunique, não peça.

Um desconto só é útil se puder ser aplicado a alguma coisa. Nossa empresa vende
livros, então como ficaria a aplicação do nosso código de desconto atual com
um produto de verdade?

    <?php

    namespace MyApp\Promotion;

    $book = new Product('Object Thinking (Developer Reference)', 60.00);
    $blackFriday = new Discount\Money(10.00);

    $finalPrice = $book->getPrice() - $blackFriday->getValue();
    $book->setPrice($finalPrice);

E se o preço do produto for menor que o desconto?

Essa pergunta cretina é a que você deveria ter feito. Elas mostram que sua
classe de desconto não encapsula o comportamento que ela promete encapsular.
Grande parte do problema disso esta no ato automático de criar os métodos de acesso
(get/set) sem pensar na comunicação de um objeto com outro.

Para nossa alegria, existe uma coisa chamada [Tell, don't ask][1] que bate
justamente nesse caso. Aplicando ele ao nosso desconto, teríamos:

    <?php

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
                $message = 'Discount is than product price.';
                throw new \UnexpectedValueException($message);
            }

            return $newPrice;
        }
    }

> Código procedural pega uma informação e depois toma uma decisão.
> Código orientado a objetos pede que objetos façam alguma coisa.
>
> -- Alec Sharp

Antes o desenvolvedor precisava saber o que fazer com aquele valor, agora
ele precisa decidir se o que ele precisa é o valor do produto com o desconto
aplicado ou não.

    <?php

    namespace MyApp\Promotion;

    $book = new Product('Object Thinking (Developer Reference)', 60.00);
    $blackFriday = new Discount\Money(10.00);

    $customerCartValue = $blackFriday->calculateProductFinalPrice($book);

Seguindo [o princípio][1] e evitando os métodos de acesso temos um código
mais coeso - que é uma palavra complicada para o quão harmoniosa a relação
das nossas classes é.

Pare pra pensar novamente o quão comunicativo é nosso código atual, além
do quão fácil é pra outro desenvolvedor alterar ele. Como nosso código
sobreviveria ao pedido de um desconto em porcentagem?

## Primeira mudança: Descontos em porcentagem

Agora precisamos aplicar um desconto em porcentagem. Refletindo sobre o
problema, não temos muito a fazer além de criar outra classe de desconto
e mudar ou pouco como o valor final do livro é calculado.

Acho sempre válido você pensar nas soluções por você, se possível envie
elas pra mim depois. Como agora não tenho muita opção, segue minha solução
pro problema:

    <?php

    namespace MyApp\Promotion\Discount;

    class Percentage
    {
        private $value = 0.00;

        public function __construct($percentageToDiscount)
        {
            $value = $percentageToDiscount / 100;
            $this->value = (float) $value;
        }

        public function calculateProductFinalPrice(Product $product)
        {
            $discountValue = $product->getPrice() * $this->value;
            $newPrice = $product->getPrice() - $discountValue;
            if ($newPrice <= 0.00) {
                $message = 'Discount is greater than product price.';
                throw new \UnexpectedValueException($message);
            }

            return $newPrice;
        }
    }

Usar o [princípio][1] força você a imaginar como um objeto vai ser usado
e nas informações que o usuário terá quando for consumir a funcionalidade
da sua classe. Pra resolver isso, eu costumo tentar fazer o [código imitar
uma conversa entre duas pessoas][ddd].

Quando você recebe um desconto, como a pessoa comunica esse desconto a você?

1. Você tem 25% de desconto em qualquer produto.
2. Você só vai pagar 75% do produto.
3. Você vai pagar o valor do produto menos o valor dele multiplicado por 0.25.

Imaginando que as três conversas fossem um código de verdade, eu penso
imediatamente nos códigos abaixo:

    <?php

    namespace MyApp\Promotion;

    // 1. Você tem 25% de desconto em qualquer produto.
    $blackFriday = new Discount\Percentage(25);

    // 2. Você só vai pagar 75% do produto.
    $blackFriday = new Discount\Percentage(75);

    // 3. Você vai pagar o valor do produto menos o valor dele multiplicado por 0.25.
    $blackFriday = new Discount\Percentage(0.25);

Qualquer um dos três códigos pode funcionar, mas qual é a real expectativa do
desenvolvedor quando for consumir o código existente?
[Deixar implementação próxima da forma como vocês conversam sobre uma
funcionalidade dentro da empresa][ddd] evita diversos problemas. Como na nossa
empresa fictícia nos comunicamos usando o primeiro caso, implementamos ele.

Repare no nome do primeiro argumento: `$percentageToDiscount`. Ele tira toda a
ambiguidade do processo e elimina a necessidade do desenvolvedor precisar ler o
resto da classe. Através de um [código limpo][3] estamos sempre evitando a ambiguidade
e a dúvida onde pudermos.

As diferenças entre os casos 1 e 2 são a forma como vocês conversam sobre a
funcionalidade. Já no caso 3 a coisa se degringola um pouco: Você expõe a conta
de porcentagem pro cliente e, além disso ser extremamente estranho no mundo real,
isso pode ser prejudicial no futuro como no caso dos métodos de acesso.

## Usando métodos de acesso (ou, o que evitar)

Vamos analisa agora o cenário de evolução acima usando os métodos de acesso.
Já vimos como aplicar os R$10 de desconto da *Black Friday* em um exemplo
anterior, mas como recordar é viver, vamos a ele:

    <?php

    namespace MyApp\Promotion;

    $book = new Product('Object Thinking (Developer Reference)', 60.00);
    $blackFriday = new Discount\Money();
    $blackFriday->setValue(10);

    $customerCartValue = $book->getPrice() - $blackFriday->getValue();
    if ($customerCartValue <= 0.00) {
        throw new \UnexpectedValueException('Deu ruim.');
    }

Como ficaria nosso código atual depois que alguém pedisse a possibilidade de
descontos utilizando porcentagem? Tenho certeza que você consegue pensar em
alguma coisa (e não esquecer de me mandar depois) mais ou menos assim:

    <?php

    namespace MyApp\Promotion;

    $book = new Product('Object Thinking (Developer Reference)', 60.00);
    $blackFriday = new Discount\Percentage();
    $blackFriday->setValue(25);

    if ($blackFriday instanceof Discount\Money) {
        $discountValue = $blackFriday->getValue();
    } else if ($blackFriday instanceof Discount\Percentage) {
        $discountValue = $book->getPrice() * ($blackFriday->getValue()/100);
    } else {
        throw new \RuntimeException('Unknown discount type.');
    }

    $customerCartValue = $book->getPrice() - $discountValue;
    if ($customerCartValue <= 0.00) {
        throw new \UnexpectedValueException('Deu ruim.');
    }

Tem como melhorar isso? Olha o tamanho desse código! São tantas linhas
pra entender e tantas condições pra interpretar que eu tenho certeza que algum
desenvolvedor no futuro vai deixar de ler alguma coisa e quebrar algo.

Eu poderia ter simplificado um pouco e feito o `Discount\Percentage::setValue()` já
fazer a conta de porcentagem como fiz no exemplo da implementação anterior. Será
que a coisa ficaria muito melhor? Vamos ver só nossa cadeia implacável de condições
como ela ficaria com essa mudança:


    <?php

    // Você sabe o que tem aqui pra cima ...

    if ($blackFriday instanceof Discount\Money) {
        $discountValue = $blackFriday->getValue();
    } else if ($blackFriday instanceof Discount\Percentage) {
        $discountValue = $book->getPrice() * $blackFriday->getValue();
    } else {
        throw new \RuntimeException('Unknown discount type.');
    }

    // ... e pra baixo também ...

Bela bosta de melhora hein champs. Comparando só o trecho de código acima (que
compreende só as condições usando métodos de acesso) contra o código abaixo (que
é o código seguindo o [princípio][1]), qual você acha mais fácil de entender?

    <?php

    namespace MyApp\Promotion;

    $book = new Product('Object Thinking (Developer Reference)', 60.00);
    $blackFriday = new Discount\Percentage(25);

    $customerCartValue = $blackFriday->calculateProductFinalPrice($book);

Alguns podem argumentar que isso é sexo dos anjos, e eu sinceramente acho essa
discussão irrelevante. A discussão relevante aqui é: Qual dos dois códigos você
acha que vai dar mais problema daqui a 4 anos?

Qual das duas situações é mais frágil à desatenção do desenvolvedor?

Com descontos é provável que seu processo de *Quality Assurance* identifique o
problema, mas tome alguns segundos e extrapole essa situação. Pressupor qualquer
conhecimento, de como consumir uma classe, vai dar em merda alguma hora. Então
[dê o conhecimento pra ele, não peça][1].

Vamos ver um caso onde a falta de atenção e os métodos de acesso vão causar problemas?

    <?php

    // Todas aquelas condições e cálculo do preço final do produto estão logo acima

    $blackFriday->setValue(75);

Com o método de acesso você pode definir outro valor de desconto. Pro mesmo desconto.
É bem óbvio que isso não afeta o preço do produto anterior, certo?

No nosso código pode ser que sim. Pense esse código num *controller* com algumas centenas
de linhas, com várias chamadas aos outros métodos de acesso em outros objetos - esses
métodos de acesso sempre vêm com vários amigos. Será que essa reciclagem de objetos seria
tão óbvia assim?

Vamos esquecer então que esse tipo de código com métodos de acesso sequer existiu
e continuar nossa tarefa de desenvolvedor + empreendedor na nossa empresa.

## Segunda mudança: Valor mínimo de um produto para desconto

Nossa empresa está dando muitos descontos e isso vai acabar com ela. A sacada agora
é só dar descontos para produtos muito caros.

Pra implementação a coisa fica menos intuitiva. Vamos lembrar o que temos
até agora:

1. Uma classe `MyApp\Promotion\Discount\Money` que é um valor monetário de desconto.
2. Uma classe `MyApp\Promotion\Discount\Percentage`.
3. Uma interface `MyApp\Promotion\Discount\DiscountInterface`.

Você, como pessoa atenta que é, reparou que eu escondi algumas evoluções no código.
Na nossa empresa, como usamos [TDD][], reparamos que todo desconto tem o mesmo
método de aplicação então extraímos ele.

    <?php

    namespace MyApp\Promotion\Discount;

    use MyApp\Promotion\Product;

    interface DiscountInterface
    {
        public function calculateProductFinalPrice(Product $product);
    }

Repare como essa *interface* é Tesuda! Qualquer desenvolvedor na empresa sabe criar
um desconto novo com ela. Só com o nome do método e com a necessidade de receber um
produto!

> Existem só duas coisas difíceis na Ciência da Computação: invalidação de cache
> e dar nome à coisas.
>
> -- Phil Karlton

Pensando na mínima mudança necessária do [TDD][], nosso código de verdade seria
mais ou menos assim:

    <?php

    namespace MyApp\Promotion;

    $minimumPriceForDiscount = 100.00;
    $blackFriday = new Discount\Percentage(75);
    $product = new Product('Refactoring to Patterns', 65.00);
    $finalPrice = $product->getPrice();
    if ($product->getPrice() > $minimumPriceForDiscount) {
        $finalPrice = $blackFriday->calculateProductFinalPrice($product);
    }

Agora precisamos deixar nosso código bonito, refatorar ele.

Como aplicar [o princípio][1] que aprendemos nisso? Podemos usar a mesma *interface*
de desconto que temos, pelo menos isso a gente sabe. Se implementarmos ela precisamos
retornar um valor de desconto além de saber qual o preço mínimo permitido. Queremos
obviamente continuar usando nossas classe de desconto atuais e futuras, além de ter
pouco trabalho. Fedeu né?

Existem várias formas de resolver um problema e espero que você tenha encontrado outras
além das que mostrei - e já as ter enviado pra mim como pedi. Vamos ver algumas soluções
que consigo pensar pra isso?

### Acrescentando um comportamento em tempo de execução

Se ao menos tivéssemos como acrescentar esse comportamento de valor mínimo a um desconto
teríamos como resolver nosso problema. [Adicionar comportamento][decorator] parece como
um problema comum que você já deve ter lido a solução em algum lugar:

    <?php

    namespace MyApp\Promotion\Discount;

    use MyApp\Promotion\Product;

    class WhenCheaperThan implements DiscountInterface
    {
        private $minimumPriceForDiscount = 0.00;
        private $discountToApply = null;

        public function __construct($minimumPriceForDiscount, DiscountInterface $applyDiscount)
        {
            $this->minimumPriceForDiscount = (float) $minimumPriceForDiscount;
            $this->discountToApply = $applyDiscount;
        }

        public function calculateProductFinalPrice(Product $product)
        {
            if ($product->getPrice() <= $this->minimumPriceForDiscount) {
                return $product->getPrice();
            }

            return $this->discountToApply->calculateProductFinalPrice($product);
        }
    }

Usar um [Decorator][] parece complicado mas é bem simples. Ele acrescenta um nível a
mais na comunicação com o objeto que queremos, o desconto, como uma casca. Nessa casca
decidimos se vamos ou não aplicar o desconto.

    <?php

    namespace MyApp\Promotion;

    $product = new Product('Refactoring to Patterns', 65.00);
    $blackFriday = new Discount\Percentage(25);
    $discountConstraint = new Discount\WhenCheaperThan(100.00, $blackFriday);

    $product = $discountConstraint->calculateProductFinalPrice($product);

Conversando com outro desenvolvedor do nosso time, [ele][nelson] apontou sobre como não
acrescentamos de fato um comportamento ao desconto mas modificamos o existente. Além de
que o uso do [decorator][] não deixa tão claro pro usuário como isso afeta um desconto.

Vamos pensar em outra solução então?

### Segregando interfaces

Vimos até agora o poder [que preferir comunicar algo ao invés de pedir][1]
têm no nosso código. Todo esse poder está exposto através de métodos, será que conseguimos
pensar em algum método que deixe claro quando um desconto pode ser aplicado ou não?

Vamos pensar em como nosso time se comunica a respeito dessa situação de desconto:

1. Damos R$5 de desconto pra todos os clientes.
2. Se o valor do produto for maior que R$50, damos 25% de desconto ao invés de R$5.

Poderíamos colocar essa condição de desconto em todas as nossas classes de desconto,
mas isso [violaria um outro princípio][srp]. Já que aparentemente existe sempre uma
condição de desconto sendo aplicado, mesmo que ela seja válida pra todos os nossos
clientes, por que não deixar essa condição explícita com um método?

    <?php

    namespace MyApp\Promotion\Discount\Condition;

    use MyApp\Promotion\Product;

    interface ApplicableToProduct
    {
        public function isApplicableToProduct(Product $product);
    }

Com essa *interface*, fica meio claro que precisamos ter algumas classes responsáveis
pode definir quando um desconto pode ser aplicado ou não. A mais fácil de fazer e pensar
é o desconto que é sempre aplicado:

    <?php

    namespace MyApp\Promotion\Discount\Condition;

    use MyApp\Promotion\Product;

    class EveryProductReceivesDiscount implements ApplicableToProduct
    {
        public function isApplicableToProduct(Product $product)
        {
            return true;
        }
    }

Enquanto a classe que define a condição a partir do preço do produto:

    <?php

    namespace MyApp\Promotion\Discount\Condition;

    use MyApp\Promotion\Product;

    class ProductsExpensivierThan implements ApplicableToProduct
    {
        private $minimumPriceRequiredForDiscount = 0.00;

        public function __construct($minimumPriceRequiredForDiscount)
        {
            $this->minimumPriceRequiredForDiscount = (float) $minimumPriceRequiredForDiscount;
        }

        public function isApplicableToProduct(Product $product)
        {
            $productPrice = $product->getPrice();
            if ($productPrice >= $this->minimumPriceRequiredForDiscount) {
                return true;
            }

            return false;
        }
    }

Agora que temos as duas diferentes formas de desconto que podemos aplicar a um produto,
temos que garantir que um desconto respeite essa condição. Precisamos então alterar nossa
interface de desconto:

    <?php

    namespace MyApp\Promotion\Discount;

    use MyApp\Promotion\Product;

    interface DiscountInterface
    {
        public function calculateProductFinalPrice(
            Product $product,
            Condition\ApplicableToProduct $discountCondition
        );
    }

Vou poupar você da mudança nas classes de desconto, que é simples na verdade. Vamos ver
como ficaria o uso disso no caso dos 25% de desconto para produtos mais caros que R$50?

    <?php

    namespace MyApp\Promotion;

    $product = new Product('Refactoring to Patterns', 65.00);
    $blackFriday = new Discount\Percentage(25);
    $ifNotTooCheap = new Discount\Condition\ProductsExpensivierThan(50.00);

    $finalPrice = $blackFriday->calculateProductFinalPrice($product, $ifNotTooCheap);

Reparando um pouco no código acima, ele realmente fica mais coeso como o [Nelson][]
esperava. O código atual conta uma história que não força o desenvolvedor que está
usando o código a saber mais nada além do que ele está lendo, ele provavelmente
consegue entender e mudar as taxas de desconto sem muito trabalho.

## Peça desculpas, não permissão

Fazer um desenvolvedor pedir por algo implica no fato dele conhecer o que precisa
ser feito. O conhecimento de todas as regras de negócio nem sempre é um requisito
conhecido e essa falta de conhecimento vai se refletir em falhas na sua aplicação.

Comunicando as ações antes de permitir um desenvolvedor a pedir as informações que
ele precisa vai ajudar você a:

- Testar unitariamente suas regras de negócio.
- Diminuir a quantidade de falhas na sua aplicação.
- Diminuir o medo de alteração, favorecendo a reutilização.
- Manter a relação entre seus objetos mais coesa (o nome bonito pra harmonia).

Existem várias coisas que omiti ou que mencionei de forma superficial aqui, mas
tentei deixar esse post o mais objetivo possível. Gostaria de agradecer imensamente
[às pessoas que revisaram e discutiram esse texto comigo][creditos], se você puder
agradeça eles também.

Além da abordagem superficial, eu devo ter cometido alguns erros. Se você por acaso
notar alguma coisa [me deixe sabendo][issues], serei eternamente grato por isso.

Se você já leu todos os links do post, comprou os livros e está esperando eles chegarem,
[existe uma discussão bacana no C2][c2-tda] sobre isso [além de um post muito melhor
que o meu][c2-acessors].

Se você leu até aqui e acha que aprendeu alguma coisa, esta louco pra começar a
tentar fazer isso no seu dia a dia. Eu sei como isso vai ser frustrante e pra
te preparar pro que você enfrentará eu deixei um método de acesso de propósito
em todos os exemplos: o preço do livro. O que você acha de tentar remover esse
método de acesso e [me mostrar o código que você bolou][gist]? Eu fui camarada
e [preparei todo código pra você][code], mereço um tweet desse post ou não?

[1]: http://martinfowler.com/bliki/TellDontAsk.html
[gist]: https://gist.github.com
[3]: http://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882
[ddd]: http://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215
[decorator]: https://sourcemaking.com/design_patterns/decorator
[explain-variables]: https://sourcemaking.com/refactoring/introduce-explaining-variable
[TDD]: http://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530
[nelson]: http://twitter.com/nelson_senna
[creditos]: https://gist.github.com/augustohp/4384b923463e947cd31b#comment-1460949
[c2-acessors]: http://c2.com/cgi/wiki?AccessorsAreEvil
[c2-tda]: http://c2.com/cgi/wiki?TellDontAsk
[singleton]: https://sourcemaking.com/design_patterns/singleton
[srp]: https://en.wikipedia.org/wiki/Single_responsibility_principle
[code]: https://gist.github.com/augustohp/fd4e4cf90df07d66b949
[issues]: https://github.com/augustohp/augustohp.github.com/issues
