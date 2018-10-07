---
title: Automatizando testes de software
layout: post
date: 2018-09-19
category: 
  - Palestra
  - PHP
excerpt:
    Uma breve descrição do que são testes automatizados, como 
    fazer seu primeiro teste e o que buscar para continuar aprendendo.
---

O [PHPUnit][1] é a ferramenta [padrão de testes no PHP][2], e após várias
tentativas anteriores de como explicar *testes automatizados em 50 minutos*
chegamos a essa iteração da tentativa, que:

1. Explica como criar sua própria ferramenta de testes
1. Como testar uma aplicação existente
1. Como transportar nossos testes para o PHPUnit

Meu objetivo com essa estrutura é mostrar que você já sabe testar. Minha
hipótese é que mostrando como automatizar um teste sem nenhuma ferramenta fica
mais fácil entender como usar o PHPUnit.

[1]: https://phpunit.de/
[2]: https://packagist.org/search/?tags=testing

## Você já sabe testar

Automatizar testes não é tão óbvio quando pode parecer e é bem difícil escrever
*bons testes* - justiça seja feita que é difícil até definir o que é um *bom
teste*. A receita pra isso é tentar, falhar e aprender com isso. Levei mais de 5
anos pra me sentir confortável com o conceito.

Você sempre checa se o que você fez funciona ou não, isso é testar. É normal
escutar pessoas dizendo que "não sabem testar" quando na verdade elas querem
dizer que não sabem fazer isso de forma automática. A exemplo o teste abaixo:

    $ echo "Hello World!"
    Hello World!

O *output* é exatamente o esperado então o teste é um sucesso! Falhas podem
acontecer de diversas formas:

    $ echp "Hello World!"
    -bash: echp: command not found

O *output* do comando acima é uma falha, por exemplo. Se você que automatizar
seus testes precisa aprender que eles possuem basicamente duas condições:
**sucesso** ou **falha**.

### Automatizando nossa primeira verificação

*Automatizar* significa criar um programa que faça essa verificação sozinho pra
nós e nos diga se tudo deu certo ou não. Daí vem a primeira confusão:

1. Uma **verificação** (*assertion*) pode ter *sucesso* ou *falha*
1. Um **teste** pode ter *sucesso* ou *falha*

Um *teste* pode ser composto por várias *verificações* e se uma *verificação*
falha o teste falha como consequência. Para automatizar o um teste precisamos
saber quais verificações podemos ou iremos fazer, seguindo o exemplo anterior
podemos verificar:

1. O *output* é igual ao esperado?
1. O comando sendo executado existe?
1. O comando é executado com sucesso?

A mim, a lista de *verificações* passíveis de automatização são uma das tarefas
mais difíceis e que nenhum *framework de teste unitário irá fazer por você*.
Implementar todas as *verificações* é uma excelente ideia mas com o tempo você
nota que existe um ideal e o ideal agora é só verificar se o *comando é
executado com sucesso*.

Toda *shell*, ao executar um comando, popula a variável `$?` com `0` (zero) caso
sucesso e é nesse comportamento que vamos verificar todo nosso comportamento:

    $ echo "a"
    a
    $ echo $?
    0
    $ echp "a"
    -bash: echp: command not found
    $ echo $?
    127

Sabendo o que precisamos *verificar*, podemos escrever nosso *teste*. Ele será
um programa *shell* que terminará com `0` (zero) no caso de sucesso além de
imprimir "ok".

```sh
#!/usr/bin/env sh

# 1. Executa o comando
# O `> /dev/null` faz com que o output do comando não seja exibido
echo "Hello World!" > /dev/null
# 2. Verificamos a saida
if [ "$?" == "0" ]
then
    # 3. Imprime sucesso
    echo "Ok"
    # 4. Sai com status 0 (zero) de sucesso
    exit 0
else
    # 3. Imprime erro
    echo "Error"
    # 4. Sai com status 1 (um) de erro
    exit 1
fi
```

Toda vez que executarmos o programa acima, ele fará a *verificação* de forma
automática. Apesar do programa acima não parecer muito útil, ele é a estratégia
que todas as ferramentas de *Integração Contínua* usam: verificar o [*exit code*
de um comando][3]. Apesar dele não parecer muito útil, você aprendeu uma lição
fundamental para fazer seu próprio sistema de *integração contínua*.

[3]: https://en.wikipedia.org/wiki/Exit_status#POSIX

### Automatizando a execução das verificações

É aqui que a maioria dos frameworks de teste entram. Apesar deles já possuírem
diversas ferramentas que auxiliam na *verificação*, o que eles inicialmente
provêm é uma *forma de organizar suas verificações* e de *executar elas*.

O [PHPUnit][1], por exemplo, trata todas as classes com sufixo `Test` e que
herdam `PHPUnit\Framework\TestCase` como uma suíte (conjunto) de testes e todo
método com o prefixo `test` como um teste. Se nós quisermos algo semelhante,
precisamos:

1. Definir uma *estrutura* padrão de teste
1. *Executar* todos os testes que seguem essa estrutura
1. Produzir um *relatório* dos testes

A *estrutura* que nossos testes terão é simples e eficiente, e não muito
diferente do que várias ferramentas oferecem: 

1. Todo teste deve estar dentro do diretório `test`
1. Um teste por arquivo, o nome do arquivo é o nome do teste
1. O teste não deve imprimir nada
1. O [exit code][3] do teste é o resultado dele

Agora precisamos de um programa para *executar todos os testes*. Esse programa,
assim como nossa *verificação automatizada* e nossos testes, irá terminar com
[exit code][3] 0 (zero) em caso de sucesso.

    $ ls tests/*.sh
    tests/hello.sh

O `ls` acima irá listar todos os arquivos `.sh` dentro do diretório `tests`,
podemos usar a saída desse comando em um `for` que será executado para cada item
encontrado:

```sh
#!/usr/bin/env

# 1. Busca todos os testes existentes
for test in $(ls tests/*.sh)
do
    # 2. Garante que o teste possa ser executado
    chmod a+x "${test}"
    # 3. Executa o teste
    $test > /dev/null
    if [ "$?" != "0" ]
    then
        # 4. Saída com status 1 (um) de erro
        exit 1
    fi
done
# 4. Saída com status 0 (zero) de sucesso
exit 0
```

Agora não importa quantos testes tenhamos no diretório `tests`, sempre que
executarmos o programa acima vamos ter o resultado de sucesso caso todas as
nossas *verificações* passem.

Falta fazer a parte de *relatório*, mas acho que você já pegou as manhas do que
estamos fazendo. Existem padrões de relatório de testes automatizados:

* [xUnit][4] é um formato em XML que costuma ser o padrão aceito
* [TAP][5] é um formato mais verboso e mais apropriado para humanos
* [TestDox][6] é um padrão para nome de testes que é usado como relatório também

[4]: https://en.wikipedia.org/wiki/XUnit#Test_result_formatter
[5]: https://testanything.org/
[6]: https://en.wikipedia.org/wiki/TestDox

Esses formatos padrão de relatório de execução são importantes só para
integração com outras ferramentas, que normalmente são ferramentas de
[Integração Contínua][ci].

[ci]: https://www.martinfowler.com/articles/continuousIntegration.html

## Para onde continuar?

Existe [um vídeo deu apresentando essa ideia e como usar o PHPUnit para
automatizar seus testes][phpcs] que vai um pouco além do escrevi aqui.

[phpcs]: https://www.eventials.com/locaweb/automatizando-testes-com-phpunit-com-augusto-pascutti/

Recomendo alguns livros também:

* [GOOS][]: Cria um software usando TDD num passo-a-passo bem fácil de entender
* [TDD][]: Descreve a técnica de criar testes automatizados antes da
  implementação e como isso pode melhorar sua vida

[goos]: https://www.amazon.com/Growing-Object-Oriented-Software-Guided-Tests/dp/0321503627
[tdd]: https://www.amazon.com/Test-Driven-Development-Kent-Beck/dp/0321146530

Se você quiser qualquer dica, ou tiver alguma crítica ou sugestão, dê um toque!
Se eu puder der uma dica a você que nunca fez um *teste automatizado* ela é a de
começar logo. Além da curva de aprendizado natural, leva um tempo aprender que
nem todo código é automaticamente testável e mais tempo ainda em como fazer isso
e os livros acima ajudam bastante a reduzir esse tempo.

## Perguntas frequentes

> Como eu convenço meu chefe de que isso é importante?

No começo desse post eu tentei explicar que você faz isso de um jeito ou de
outro. Começar a fazer testes de maneira automática reduz o **seu trabalho** e
se tudo der certo você vai começar a entregar trabalho com mais qualidade.

Se você precisa aprender a fazer testes automáticos, daí a conversa com seu
gestor é outra.

> Como eu testo algo que já existe e o código é ruim?

Você pode usar [testes de comportamento][bdd] para testar a aplicação inteira.
Eles são mais lentos e precisam de algumas condições anteriores (usuário
existir, produto, etc) mas vão entregar valor rápido e costumam ser mais simples
de entender e fazer no início.

[bdd]: https://en.wikipedia.org/wiki/Behavior-driven_development

<!--
vim: spell spelllang=pt
-->
