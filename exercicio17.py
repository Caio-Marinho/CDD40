somaImpar = 0
for x in range(1,11):
    numero = int(input(f"Digite o {x}º numero: "))
    if numero%2!=0:
        somaImpar+=numero
print(f"A soma total dos valores impares é igual a {somaImpar}")