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
                f.write('#include <stdio.h>\n')
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

    while True:
        print('\nVocê quer criar uma função?\n')
        print('[0] - Sim\n[1] - Não\n')
        choice = int(input('>>> '))
        if choice == 1: break
        elif choice == 0:
            print('\nQual será o valor retornado pela função?')
            value = input('>>> ')
            print('\nQual será o nome da função? ')
            nome = input('>>> ')

            argl = []
            print('\nEscreva os argumentos (não se esqueça dos seus valores). Digite "sair" quando terminar.\n') # arrumar essa macarronada de codigo
            while True:
                arg = input('>>> ')
                if arg == 'sair': break
                else:
                    argl.append(arg)
                    continue

            args = ', '.join(str(i) for i in argl)

            customfunc(name, nome, value, str(args))
        else:
            print('Tente novamente.')
            quit()
    
    with open(f'{name}.c', 'a') as f: f.write('int main() {\n')
    print('\nDigite seu código abaixo.\nPs: digite "sair" para fechar o programa.\n')

    while True:
        linha = input('>>> ')

        if linha == 'sair':
            with open(f'{name}.c', 'a') as f:
                f.write('}')
            
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

def customfunc(file, name, value, *args): # consertar aq com os argumentos etc.
    with open(f'{file}.c', 'a') as f: f.write('{} {}({})'.format(value, name, *args))
    with open(f'{file}.c', 'a') as f: f.write('{\n')

    print('\nDigite seu código abaixo.\nPs: digite "end func" para encerrar a função e continuar ao código')

    while True: 
        line = input('>>> ')

        if line == 'end func':
            with open(f'{file}.c', 'a') as f: f.write('}\n')
            print('\nFunção criada!\n')
            break

        if line != '' and line[-1] != ';': line += ';'

        with open(f'{file}.c', 'a') as f:
            f.write(f'{line}\n')
        continue
        

if __name__ == '__main__':
    code('main')