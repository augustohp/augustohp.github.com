---
title: phpunit
layout: post
date: 2017-07-02
category:
---

O [PHPUnit][] é a ferramenta de testes mais utilizada em projetos PHP. Agreguei
algumas dicas direto das trincheiras de quem usa ela há pelo menos 7 anos.

Um *aviso* aos leitores de como pretendo fazer isso: além de passar algumas
*boas práticas*, quero que todos entendam como a ferramenta funciona e o porquê
dela existir, pra isso quero apresentar os problemas que uma ferramementa de
testes deveria resolver. Faço isso não porque acho necessário, mas por
incapacidade de sintetizar tudo que aprendi sem ligar as soluções aos problemas
- e por isso, já peço desculpas.

[phpunit]: https://phpunit.de
[composer]: https://getcomposer.org

## Ambiente de desenvolvimento

É pra ser uma coisa bem óbvia, mas [aparentemente não é][1]. Existem algumas
formas de se usar o [PHPUnit][], a melhor? Através do [Composer][], localmente
em um projeto, como dependência de desenvolvimento.

A vantagem de se usar o [PHPUnit][] diretamente como dependência do projeto faz
com que você não fique brigando com *constraints* de versão dele. Alguma vez
você irá trabalhar mantendo um projeto em PHP 7 e outro em PHP 5, o que vai te
possibilitar depender de 2 versões diferentes do [PHPUnit][]. Se você instalou
ele de forma [global][composer-global], você pode não conseguir rodar sua suite
de testes em alguns de seus projetos.

Pra instalar o [PHPUnit][] localmente no projeto é bem simples:

    $ composer.phar require --dev --no-interaction phpunit/phpunit

A opção `--dev` garante que a dependência do [PHPUnit][] será listada só para o
ambiente de desenvolvimento - isso se você fizer o deploy da sua aplicação com
`composer.phar install --no-dev`.

Eu gosto de executar a suite de testes do projeto com um único comando.
Dependendo do projeto, você pode ter suites funcionais ou vários comandos que
compõem sua sua suite de testes. O [Composer][] tem uma coisa chamada [Composer
Scripts][composer-scripts], que basicamente te possibilita criar comandos que
ficam disponíveis quando você chamada o comando `composer.phar` dentro da raiz
do projeto, no nosso caso vamos criar o subcomando `composer.phar test` editando
o `composer.json`:

    {
        "require-dev": {
            "phpunit/phpunit": "^5.7"
        },
        "scripts": {
            "test": [
                "phpunit"
            ]
        }
    }

Boa! Agora precisamos configurar o [PHPUnit][]. A melhor forma de fazer isso é
com um `phpunit.xml.dist` na raiz do projeto, o [PHPUnit][] tenta encontrar ele
depois de um `phpunit.xml`. Servindo o arquivo `phpunit.xml.dist` como padrão e
colocando o `phpunit.xml` no `.gitignore`, todo desenvolvedor consegue manter
suas preferências de como ele quer rodar aquela suite de testes mas se o
*padrão* (`phpunit.xml.dist`) for bom o suficiente pra ele então ele pode só
ignorar isso. Eu normalmente copio o arquivo do próprio [PHPUnit][]:

    $ cp vendor/phpunit/phpunit/phpunit.xml phpunit.xml.dist

Dou uma editada rápida no arquivo pra declarar o nó do `<php>` definindo algumas
configurações padrões - mantendo a suite de testes independente da configuração
da máquina:

* `date.timezone` é obrigatório. Sem ela, qualquer código dependente de funções
  de data terminará num *warning*.
* `display_errors` não é obrigatório mas é o comportamento que você espera de um
  código sendo testado: você quer ver os erros.
* `error_reporting=-1` garante que iremos ser reportados de todo tipo de erro.
  *Notices* e *deprecations* são erros comuns de serem ignorados, mas que
  geralmente são simples de se resolver e envolvem ganhos substanciais quando
  utilizamos versões mais novas do PHP.

    <?xml version="1.0" encoding="UTF-8"?>
    <phpunit xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:noNamespaceSchemaLocation="phpunit.xsd"
            bootstrap="vendor/autoload.php"
            backupGlobals="false"
            verbose="true">
        <testsuites>
            <testsuite name="small" />
                <directory suffix="Test.php">tests/unit</directory>
            </testsuite>
        </testsuites>

        <filter>
            <whitelist processUncoveredFilesFromWhitelist="true">
                <directory suffix=".php">src</directory>
            </whitelist>
        </filter>

        <php>
            <ini name="date.timezone" value="UTC"/>
            <ini name="display_errors" value="1"/>
            <ini name="error_reporting" value="-1"/>
        </php>
    </phpunit>

Essa estrutura básica garante a você felicidade:

* Testes automáticos podem ser executados através de `composer.phar test`.
* Configurações básicas do PHP são garantidas para aquele projeto específico.
* Desenvolvedores têm a liberdade de configurar a suite e manter essa
  configuração.
* Disponibiliza **todas as suites** na raiz do projeto. Executando `phpunit` na
  raiz do projeto deve executar todas as suítes disponíveis.

[1]: https://twitter.com/s_bergmann/status/879717962634203136 "PHPUnit usage in production"

# Por que automatizar testes?

Sendo direto: eles facilitam mudanças. Um [sistema difícil de mudar é
complexo][2] - o que pode parecer óbvio mas não é se você pára para pensar em
todo débito técnico já negligenciado por você na sua carreira.

Me sinto na obrigação de avisar que ter uma suíte de testes automatizada, por si
só, não garante nada. Como ferramenta, a função dela é colaborar com o resto do
time a manter a aplicação. Existem sinais de que uma suite automatizada não está
te ajudando quando:

* Ela leva mais tempo pra ser executada na sua máquina do que você está disposto
  a esperar - observando ela sendo executada.
* Mudanças nas regras de negócio que não quebram nenhum teste.

Automatizar é trabalho da equipe de desenvolvimento, então não é bacana delegar
essa decisão a galera de negócio. O time de desenvolvimento deve entender que
testes serão feitos, num ambiente e equipe pra isso ou em produção pelos
clientes finais, automatizar eles não aumenta a qualidade porque impede erros de
acontecerem. Testes automatizados aumentam a qualidade porque forçamos os erros
acontecerem antes de outras pessoas notarem, e a beleza dessa prática está no
tempo: um teste automatizado nunca é esquecido.

Não delegue a decisão de automatizar testes a outro time. Não tente nem
argumentar, você já está perdendo tempo precioso não praticando. O aprendizado é
longo e não é óbvio, nem fácil, mas ele é essencial.

[2]:  https://martinfowler.com/articles/zaninotto.pdf "Irreversibility is one of prime drivers of complexity"

## O que é um teste?

Pergunta babaca, com uma resposta nada babaca. Vamos fazer um teste simples
juntos, sem nenhuma ferramenta e ver se entendemos isso:

    <?php

    echo "Hello World!" . PHP_EOL ;

Dado o programa acima num arquivo `hello.php`, vamos executar ele e ver se ele
gera o que esperamos:

    $ php hello.php
    Hello World!
    $

Parabéns, você fez um *teste*. Só de verificar, pessoalmente e manualmente, um
comportamento você testou. Você testa várias coisas diariamente, se um commit
deu certo, se declarar uma dependência foi bem sucedida, se salvar um arquivo
foi efetivo, etc. Automatizar esse processo requer uma atenção especial a esse
tipo de comportamento seu, comece a prestar atenção a todos os testes que você
executa de forma inconciente e a estrada vai ser um pouco mais suave.

Automatizar essa bomba, e agora? Um aprendiz de testes começa checando sempre se
uma execução deu certo, e ninguém deveria ter nada contra essa prática. Vamos
escrever um programa pra checar isso:

    <?php

    $programs = [
        __DIR__ . '/hello.php'
    ];
    
    foreach ($programs as $program) {
        $output = '';
        $exitCode = 255;
        $test = 'php ' . $program;
        $lastLine = exec($test, $output, $exitCode);
        echo ($exitCode === 0) ? '.' : 'E' ;
    }

    echo PHP_EOL ;

Todo programa executado num terminal tem um *exit code*. Se o *exit code* for 0
(zero) significa que o programa rodou com sucesso, o que pode ser usado para
testar muita coisa. O programa acima usufrui desse comportamento, pegando uma
lista de programas PHP e executando todos eles, qualquer *exit code* diferente
de zero é tratado como erro.

Existem diversas melhorias óbvias, como atrelar uma verificação mais específica
a cada teste. No nosso caso, podemos comparar o output gerado a um esperado.
Outra melhoria, também óbvia, seria melhorar o *output* do programa de testes
indicando qual teste deu problema e porquê.

## Comunicando melhor as falhas


# PHPUnit pra que te quero?

* Executando testes:
    * Múltiplas suítes: rápida e lenta.
    * Quem quer qual output?
* Verificações:
    * Mensagens de verificação.
    * Verificações específicas.
    * Erros do PHP.
    * Exceptions.
* Estados de um teste:
    * Incompleto.
    * Ignorado.
    * Dependente.
    * Cobertura de código específica.
    * Isolamento pra testes específicos.
* Evitando repetir passos:
    * `setUp` e `tearDown`.
    * Provedores de dados.
* Testes com banco de dados, serviços ou dependências externas:
    * Data set/table.
    * Stubs.
    * Mocks:
        * Interfaces.
        * Classes.
        * Traits.
        * File system.

# Brincando bem com outros ecossistemas

* Wordpress
* Symfony
* ZendFramework
* Laravel

# Quero aprender mais!

1. Comece a reparar nos testes que você faz manualmente no dia a dia.
1. Como você comunicaria as falhas para novos desenvolvedores?
1. Como fazer seus testes automatizados sofrerem menos mudanças?
1. Como fazer sua suite de testes rodar mais rápido?

<!--
vim: spell spelllang=pt
-->
