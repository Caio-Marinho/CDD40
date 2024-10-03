lista = [0]*5
tamanho = len(lista)
soma = 0
cont = 0
for i in range(tamanho):
    lista[i] = int(input("Digite o valor: "))
for par in range(tamanho):
    if lista[par]%2==0:
        print(lista[par],end=' ->')
print()
for j in range(tamanho):
    for x in range(tamanho-1):
        if lista[x] < lista[x+1]:
            lista[x],lista[x+1] = lista[x+1],lista[x]
print(f"O maior é {lista[0]} e o menor é {lista[tamanho-1]}")
for y in range(tamanho):
    soma+=lista[y]
media = soma/tamanho
for i in range(tamanho):
    if lista[i]>media:
        cont+=1
print(f"Tem um total de {cont} valor acima de {media} que é a media de valores")
