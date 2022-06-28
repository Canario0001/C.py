#!/usr/bin/env python3

def code(name):
    print('Digite as bibliotecas que você vai usar.\n')
    print('Digite "init" se quiser usar APENAS a biblioteca inicial.')
    print('Digite "q" se escrever todas as bibliotecas que vai usar.')
    print('Digite "hypo" se quiser uma calculadora já pronta de hipotenusa.')
    print('Digite "hello" se quiser um olá mundo já pronto.')
    print('PS: não se esqueça de colocar .h e <> se a biblioteca possuir isso.\n')

    while True:
        library = input('>>> ').strip()

        if library == 'q': break

        elif library == 'init':
            with open(f'{name}.c', 'w') as f:
                f.write('#include <stdio.h>\n\nint main() {\n')
            break

        elif library == 'hypo':
            hypocode(name)
            print(f'Calculadora criada! Procure por {name}.c na pasta.')
            quit()

        elif library == 'hello':
            hellocode(name)
            print(f'Olá mundo criado! Procure por {name}.c na pasta.')
            quit()

        else:
            with open(f'{name}.c', 'a') as f:
                f.write(f'#include {library}\n')
            continue

    print('\nDigite seu código abaixo.\nPs: digite "sair" para fechar o programa.\n')

    while True:
        linha = input('>>> ')

        if linha == 'sair':
            with open(f'{name}.c', 'a') as f:
                f.write('}\n')
            
            print(f'\nArquivo criado! Procure por {name}.c na pasta.')
            break

        if linha != '' and linha[-1] != ';': linha += ';'
        
        with open(f'{name}.c', 'a') as f:
            f.write(f'{linha}\n')
        continue

def hypocode(name):
    with open(f'{name}.c', 'w') as f:
        f.write('#include <stdio.h>\n#include <math.h>\nint main(){\ndouble a; double b;\nprintf("Coloque o lado A: "); scanf("%lf", &a);\nprintf("Coloque o lado B: "); scanf("%lf", &b);\nprintf("Lado C: %lf", sqrt(a*a+b*b));\nreturn 0;\n}')

def hellocode(name):
    with open(f'{name}.c', 'w') as f:
        f.write('#include <stdio.h>\nint main(){\nprintf("Olá, mundo!"); return 0;\n}')

if __name__ == '__main__':
    code('main')