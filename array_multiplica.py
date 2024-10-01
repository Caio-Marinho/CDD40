arrayOriginal = [0.0]*10
arrayMulti = [0.0]*10
tamanho = len(arrayOriginal)

for i in range(tamanho):
    arrayOriginal[i] = float(input(f"Digite o {i+1}º: "))
multi = float(input("Digite qual valor sera multiplicado: "))
for m in range(tamanho):
    arrayMulti[m] = arrayOriginal[m] * multi
print(arrayOriginal)
print(arrayMulti)
