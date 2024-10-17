from Biblioteca import *

while True:
    lista = ['Inserir','Mostrar','Sair']
    for indice,item in enumerate(lista):
        print(f"{indice+1}. {item}")
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
    else:
        print("Insira um codigo válido")