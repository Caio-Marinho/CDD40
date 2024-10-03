numeros = [0]*10
tamanho = len(numeros)
for pso in range(tamanho):
    numeros[pso] = int(input(f"Digite o {pso+1}º número: "))
numero = int(input("Digite um numero qualquer: "))
qtd_numero = 0
for qtd in range(tamanho):
    if numero == numeros[qtd]:
        qtd_numero+=1
print(f"O número {numero} apareceu {qtd_numero} vezes")