---
layout: post
title: Singleton \#not
date: 2011-09-06
category: PHP, design patterns
published: true
---

Se você tiver preguiça de ler, leia só isso: Evite usar o Singleon. Ele
tem seu uso, como está descrito no livro [Design
Patterns](http://www.amazon.com/o/asin/0201633612), mas pra variar a
galera simplesmente ignorou o que tá escrito lá e saiu usando isso de
maneira leviana.

Se eu não te convenci, pense nos bebês foca. Cada vez que você
implementa o Singleton, um bebê foca é violentamente torturado e morto
por alguma gangue extremista de uma região remota da Terra.

Se eu ainda não te convenci, desculpas. Você vai ter que ler mais um
pouco!

## Singleton: A definição

Todo Design Pattern segue uma estrutura comum:

-   Qual o problema a ser resolvido
-   Uma estrutura descrita em UML
-   Um exemplo de implementação

Então vamos a razão de tanta atrocidade em relação aos bebês foca!

### Sigleton: Qual problema ele resolve

Existem casos (e sim, os malditos são poucos mas existem) em que
precisamos garantir que temos uma instância só de um objeto.

Isso vai contra todo o princípio da Orientação a Objetos, mas - de novo
-, existem casos em que precisamos que uma classe não tenha uma penca de
instâncias. Um filho bastardo já é merda o suficiente, então precisamos
garantir que só ele exista!

### Singleton: Mostrando o filho bastardo pro mundo

![Diagrama de Classe: Implementação de um Singleton](/res/img/singleton-uml.png "Diagrama de Classe: Implementação de um Singleton")

A implementação de um Singleton é essa. A classe tem um atributo que
guarda a nossa única instância, um método garante o acesso a essa
instância e o construtor da classe deve ser privado.

Ele ser privado garante que a classe não consiga ser instanciada fora
dela. Galere, lembrando que no PHP se você coloca um construtor como
*private*, você não consegue instanciar a classe! O que é exatamente o
que queremos. Controle de natalidade \#ftw!

## Onde o controle de natalidade falha

A primeira falha do Singleton, não está nele. Está nas pessoas que
implementam ele. Elas confudem o problema com um problema que elas têm
hoje. Acham de forma ignorante que o Singleton vai resolver o problema
delas.

Vamos entender de novo pra que serve o Singleton: precisamos ter uma
instância só de uma classe.\
Você entendeu bem esse problema? Tem certeza?! Vou te mostrar como você
ainda não entendeu o problema:

```php
<?php
class Zend_Controller_Front
{
    // ....
    /**
     * Singleton instance
     *
     * @return Zend_Controller_Front
     */
    public static function getInstance()
    {
        if (null === self::$_instance) {
            self::$_instance = new self();
        }

        return self::$_instance;
    }
}
```

O uso do Singleton aí em cima é de um exemplo real. Do Zend Framework.
Ele está certo? Não.

Porque não!? Eu não vou entrar no mérito de discutir o que é o
[FrontController](http://java.sun.com/blueprints/patterns/FrontController.html),
mas eu explico pra vocês.

Front Controller é um Design Pattern que resolve o problema de ser o
único ponto onde as requisições são feitas.

Agora encontrem o erro nas peças:

-   Único ponto de entrada de requisições
-   Única instância de uma classe

As peças são iguais? Não! Então porque PORRA tem um singleton
implementado no Front Controller do Zend Framework? Essa é uma boa
questão.

## Os problemas só começaram

Eu sinceramente não entendo o porquê do Singleton no Front Controller,
mas olha o tipo de problema que ele gera:

```php
<?php
class Zend_Controller_Front
{
    // ....
    /**
     * Resets all object properties of the singleton instance
     * Primarily used for testing; could be used to chain front controllers.
     * Also resets action helper broker, clearing all registered helpers.
     *
     * @return void
     */
    public function resetInstance()
    {
        $reflection = new ReflectionObject($this);
        foreach ($reflection->getProperties() as $property) {
            $name = $property->getName();
            switch ($name) {
                case '_instance':
                    break;
                case '_controllerDir':
                case '_invokeParams':
                    $this->{$name} = array();
                    break;
                case '_plugins':
                    $this->{$name} = new Zend_Controller_Plugin_Broker();
                    break;
                case '_throwExceptions':
                case '_returnResponse':
                    $this->{$name} = false;
                    break;
                case '_moduleControllerDirectoryName':
                    $this->{$name} = 'controllers';
                    break;
                default:
                    $this->{$name} = null;
                    break;
            }
        }
        Zend_Controller_Action_HelperBroker::resetHelpers();
    }
}
```

A gente precisa de um método, que "simule" a criação de uma nova
instância da classe. Porque precisamos disso se é só dar um *new* e tá
tudo certo? Porque fizemos um Singleton.

Pior! No Zend Framerk, o FrontController não implementa Singleton porque
ele permite que a classe seja instanciada fora dela! Porque? Também não
sei.

No mínimo existem umas 50 linhas relacionadas ao
Singleton-que-não-é-singleton que não tem função nenhuma no código a não
ser piorar tudo!

## As outras faces do Singleton

Sério, eu poderia escrever dias sobre os problemas que o Singleton pode
trazer pra sua vida, mas vou me ater a listar apenas alguns pontos que
me vém a mente agora:

-   Ele vai contra todo o conceito de Orientação a Objetos
-   Uma classe que implementa Singleton simplesmente é um PARTO de
    extender
-   Você não tem controle sobre a instância. Qualquer imbecil pode usar
    ela a qualquer momento, jogar alguma coisa ou até mudar alguma coisa
    sem que você saiba. Ok, você pode saber, mas vai ser tarde demais
-   Por causa do ponto acima, testar um Singleton com 100% de isolação é
    praticamente impossível
-   As pessoas tendem a confundir o Singleton com a necessidade de
    métodos estáticos (que também são uma merda)
-   Você gasta memória sem precisar. Sério, você não usa aquela
    instância Chuck Norris de Singleton durante todo o tempo que você
    obrigou ela a ficar lá te esperando na memória.
-   Pessoal tende a usar Singleton em uma classe que simplesmente é um
    repositório de métodos aleatórios pra resolver problemas genéricos
    demais (dica: Uma classe que pode ser instanciada deve sempre ser
    especificação de algo, nunca generalização)

## Conclusão

Don't fucking use Singleton! Vá ler mais sobre Design Patterns! Vá
entender realmente o que é Orientação a Objetos antes de sair
convertendo um código procedural dentro de classes e chamar isso de
Orientação a Objetos.

Revise o que outros desenvolvedores já fizeram e chegue em SUAS
conclusões. Garanto pra você que elas serão muito melhores que as
minhas! Aliás, espero elas hein!

Tem muito lixo por aí, mas não quero desemerecer quem fez as coisas. No
fim, a diferença entre eles (Zend Framework, por exemplo) e nós é que
eles fizeram. Nós não.

## Você deveria ler também

Reuni alguns posts que valem ser lidos que achei em uma busca rápida
pelo santo Google. São pessoas muito mais inteligentes que eu e você,
muito mais experientes e que provavelmente sabem o que estão falando.

-   [Singleton considerado
    estúpido](https://sites.google.com/site/steveyegge2/singleton-considered-stupid)
-   [Porque evitar o uso do
    Singleton](http://www.as3dp.com/2008/11/26/we-don%E2%80%99t-need-no-stinkin%E2%80%99-singletons-why-to-avoid-the-singleton-pattern-in-actionscript-30-programming)
