def code(lines, file_name):
    with open(f"{file_name}.c", "w") as f:
        f.write("#include <stdio.h>\n\nint main() {\n")

    for line in range(lines):
        linha = input(">>> ")

        if linha[-1] != ";": linha += ";"

        with open(f"{file_name}.c", "a") as f:
            f.write(f"{linha}\n")

    with open(f"{file_name}.c", "a") as f:
        f.write("}")

if __name__ == '__main__':
    print("Quantas linhas você quer?")
    linhas = int(input(">>> "))
    print("\nQual será o nome do arquivo?")
    nome = input(">>> ")

    print("\nDigite seu código abaixo.\n")
    code(linhas, nome)
    print("\nArquivo criado! Procure por {}.c no diretório.".format(nome))