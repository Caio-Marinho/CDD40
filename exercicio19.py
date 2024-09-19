numeroAluno = int(input("Digite o numero de alunos: "))
soma = 0
n = 1
while n<=numeroAluno:
    nota = float(input(f"Informe a nota do {n}º aluno: "))
    soma+=nota
    n+=1
media = soma/numeroAluno
print(f"A média total da sala foi de {media:.2f} pontos")
