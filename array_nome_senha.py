nomes = ['']*5
senhas = ['']*5
tamanho = len(nomes)
for i in range(tamanho):
    nomes[i] = input("Digite o nome: ")
    senhas[i] = input("Digite a senha: ")
for j in range(tamanho):
    print(f"No Índice {j}, O usuário {nomes[j]} tem a senha {senhas[j]}")