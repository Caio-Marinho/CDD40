arrayNota = [0.0]*5
tamanho = len(arrayNota)
qtd_aluno = 0
soma = 0
for posicao in range(tamanho):
    arrayNota[posicao] = float(input(f"Digite a nota do {posicao+1}º Aluno: "))
for x in range(tamanho):
    soma+=arrayNota[x]
media = soma/tamanho
for maior in range(tamanho):
    if media < arrayNota[maior]:
        qtd_aluno+=1
print(f"Foi um total de {qtd_aluno} Aluno(s) que tiraram nota maior que a media que foi {media:.2f}")
