# C.py

Esse é um projeto para escrever código C em Python.

O programa está crescendo e aceito colaboradores.

O script automaticamente adiciona a função main com as chaves e as bibliotecas de sua escolha. Todavia, o "return 0" deve ser colocado manualmente.

## Uso

Para usar, coloque o arquivo na mesma pasta que seu arquivo principal (normalmente, main.py) e então importe. O código, no momento, só será adicionado por meio de inputs na hora que estiver rodando.

Exemplo:

```py
from c import code

# nome é o nome do arquivo

code(nome)
```

Também é possível rodar diretamente o `c.py`. Ele irá perguntar o nome do arquivo.

Recomendo o uso de Python 3.7 para cima.

## Compilar

Atualmente, o programa é capaz de compilar o código em C. Entretanto, é necessário que o usuário tenha G++ instalado.

Em sistemas tipo Unix ou macOS é necessário que o compilador (`compy`) tenha permissão para executar. Normalmente, é usado o comando abaixo:

```sh
$ chmod +x compy
```

Infelizmente, por utilizar um script em bash para compilar, o programa não consegue compilar o código para Windows. Neste caso, recomendo o uso de ferramentas como o GCC, G++ ou Clang.

## Updates

Versão 1.1:
- Número ilimitado de linhas
- Bibliotecas a escolha do usuário

Versão 1.2:
- Criação de protótipos, sendo eles:
    - Calculadora de hipotenusa
    - Olá mundo

Versão 1.3:
- Limpeza do código
- Funções personalizadas pelo usuário

Versão 1.4: 
- Compilação e autoexecução do código

## Agradecimentos

Quero agradecer meu amigo [Bergeno](https://github.com/bergeno) por me motivar a colocar esse projeto aqui, no GitHub.