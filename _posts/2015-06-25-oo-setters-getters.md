---
layout: post
title: Orientação a Objetos - Um caso contra os métodos de acesso
category: Orientação a Objetos
---

Quanto de suas classes são compostas por métodos para definir e retornar valores
guardados nela? Você já questionou o benefício da orientação a objetos enquanto
estava criando uma classe?

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

Outra forma de resolver isso é utilizar comentários. Eu aprendi que o destino de
um comentário é ser ignorado ou ficar desatualizado então, como a gente resolve
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

Eu poderia ter [usado as variáveis e atributos pra explicar o que eles devem
conter][explain-variables], mas criei uma *namespace* intermediária além de
mudar o nome da classe pra deixar claro que iremos precisar de outros tipos
de desconto.

O [João Batista Neto][joao] argumentou que obrigar os demais desenvolvedores a
olhar um atributo pra descobrir o que ele é quebra a regra de encapsulamento.
Por isso optei por expressar isso no nome da classe e no argumento do construtor.
Quebrando encapsulamento ou não, o argumento do construtor sempre irá tanger o
escopo de fora da classe e a interno, agradando tanto a mim e [ao João][joao].

> Existem só duas coisas difíceis na Ciência da Computação: invalidação de cache
> e dar nome à coisas.
>
> -- Phil Karlton

Tem [uma galera][ddd] que vai muito além de querer [contar uma história][3] e
defende o estebecimento e uso de termos muito bem definidos no seu código, então
- eu acho que - é uma boa ideia você começar a prestar mais atenção nisso.

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

PS: Existe [um post muito melhor][c2-acessors] no sempre excelente
[Cunningham & Cunningham Wiki][c2] sobre isso. Sugiro que você ignore ele e
continue confiando somente em mim! Óbvio que não, vai lá ler essa porra agora!

PPS: Preciso agradecer imensamente a paciência e amizade dos amigos [Nelson][],
[João][joao], [Cobucci][] e [Ivo Nascimento][ivo] que me ajudaram muito revisando
e discutindo esse post (e provavelmente mais alguns que virão). Se você curtiu
esse post, por favor agradeça a elas por mim também! :)

[3]: https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882
[ddd]: https://www.amazon.com/Domain-Driven-Design-Tackling-Complexity-Software/dp/0321125215
[explain-variables]: https://sourcemaking.com/refactoring/introduce-explaining-variable
[singleton]: https://sourcemaking.com/design_patterns/singleton
[c2]: https://c2.com/cgi/wiki?WelcomeVisitors
[c2-acessors]: https://c2.com/cgi/wiki?AccessorsAreEvil
[pola]: https://en.wikipedia.org/wiki/Principle_of_least_astonishment
[code review]: https://en.wikipedia.org/wiki/Code_review
[joao]: https://github.com/netojoaobatista/
[nelson]: https://twitter.com/nelson_senna
[cobucci]: https://github.com/lcobucci
[ivo]: https://twitter.com/ivonascimento
