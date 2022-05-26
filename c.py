def code(name):
    print('Digite as bibliotecas que você vai usar.\n')
    print('Digite "init" se quiser usar APENAS a biblioteca inicial.')
    print('Digite "q" se escrever todas as bibliotecas que vai usar.')
    print('PS: não se esqueça de colocar .h e <> se a biblioteca possuir isso.\n')

    while True:
        library = input('>>> ').strip()

        if library == 'q': break

        elif library == 'init':
            with open(f'{name}.c', 'w') as f:
                f.write('#include <stdio.h>\n\nint main() {\n')
            break

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

        if linha[-1] != ';': linha += ';'
        with open(f'{name}.c', 'a') as f:
            f.write(f'{linha}\n')
        continue

if __name__ == '__main__':
    code('main')
