from Biblioteca import *

while True:
    lista = ['Inserir','Mostrar','Sair','Pesquisar']
    for indice,item in enumerate(lista):
        print(f"{indice+1}. {item}")
    try:
        opcao = int(input("Digite o codigo da opção: "))
        if opcao == 1:
            cadastra(input("Digite um texto: "))
        elif opcao == 2:
            leitura = mostrar()
            for texto in leitura:
                print(texto)
        elif opcao == 3:
            print("Fim de Execução!!")
            break
        elif opcao == 4:
            x = pesquisar(input("Digite o que desenja pesquisar: "))
            print(x)
        else:
            print("Insira um codigo válido")
    except ValueError:
        print("Digite um codigo")
