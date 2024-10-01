listaAlunos = ['']*5
tamanho = len(listaAlunos)
for i in range(tamanho):
    listaAlunos[i] = input(f"Digite o nome do {i+1}º aluno : ")

for indice in range(tamanho) :
    print(indice,listaAlunos[indice])