#!/usr/bin/env python3
from os import system

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
            escrever(f'{name}.c', 'w', '#include <stdio.h>\n')
            break

        elif library == 'hypo':
            hypocode(name)
            print(f'Calculadora criada! Procure por {name} na pasta.')
            quit()

        elif library == 'hello':
            hellocode(name)
            print(f'Olá mundo criado! Procure por {name} na pasta.')
            quit()

        else:
            escrever(f'{name}.c', 'a', f'#include {library}\n')
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
            print('\nEscreva os argumentos (não se esqueça dos seus valores). Digite "sair" quando terminar.\n') 
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
    
    escrever(f'{name}.c', 'a', 'int main() {\n')
    print('\nDigite seu código abaixo.\nPs: digite "sair" para fechar o programa.\n')

    while True:
        linha = input('>>> ')

        if linha == 'sair':
            escrever(f'{name}.c', 'a', '}')
            
            print('\nArquivo criado! Você quer compilar ele?')
            print('[0] - Não, não quero compilar ele.\n[1] - Sim, quero compilar ele.')
            compile = int(input('>>> '))

            if compile == 1:
                print('\nVocê quer executar ele também?')
                print('[0] - Não, não quero executar.\n[1] - Sim, também quero executar.')
                run = int(input('>>> '))

                if run == 0:
                    print(f'\nOK! Procure por {name} na pasta.')
                    system(f'./compy {name} 0')
                
                elif run == 1:
                    print('')
                    system(f'./compy {name} 1')
                
                else:
                    print('Tente novamente.')
                    quit()
            
            elif compile == 0: print(f'\nOK! Procure por {name}.c na pasta')

            else:
                print('Tente novamente.')
                quit()

            break
            

        if linha != '' and linha[-1] != ';' and linha[-1] != '{' and linha[-1] != '}': linha += ';'
        
        escrever(f'{name}.c', 'a', f'{linha}\n')
        continue

def hypocode(name):
    escrever(f'{name}.c', 'w', '#include <stdio.h>\n#include <math.h>\nint main(){\ndouble a; double b;\nprintf("Coloque o lado A: "); scanf("%lf", &a);\nprintf("Coloque o lado B: "); scanf("%lf", &b);\nprintf("Lado C: %lf", sqrt(a*a+b*b));\nreturn 0;\n}')
    
    system(f'./compy {name} 0')

def hellocode(name):
    escrever(f'{name}.c', 'w', '#include <stdio.h>\nint main(){\nprintf("Olá, mundo!"); return 1;\n}')

    system(f'./compy {name} 0')

def customfunc(file, name, value, *args):
    escrever(f'{file}.c', 'a', '{} {}({})'.format(value, name, *args))

    print('\nDigite seu código abaixo.\nPs: digite "end func" para encerrar a função e continuar ao código')

    while True: 
        line = input('>>> ')

        if line == 'end func':
            escrever(f'{file}.c', 'a', '}\n')
            print('\nFunção criada!\n')
            break

        if line != '' and line[-1] != ';': line += ';'

        escrever(f'{file}.c', 'a', f'{line}\n')
        continue
        
def escrever(file:str, mode:str, text:str):
    with open(file, mode) as f: f.write(text)

if __name__ == '__main__':
    code('main')