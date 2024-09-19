totalAlunos = int(input("Informe o total de alunos: "))
somaNota = 0
for i in range(1,totalAlunos+1):
    notaAlunos = float(input(f"Informe a nota do {i}º aluno: "))
    somaNota+=notaAlunos
media = somaNota/totalAlunos
print(f"A média total da sala foi de {media:.2f} pontos")