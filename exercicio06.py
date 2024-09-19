"""Duas variáveis (A e B) possuem valores distintos (A=5
e B= 10), crie um algoritmo que armazene esses
dois valores nessas duas variáveis, e efetue a troca
dos valores de forma que a variável A passe a
possuir o valor da variável B e que a variável B
passe a possuir o valor da variável A. Por fim,
apresentar os valores trocados."""
valorA = 10
valorB = 5
print(f"\nO valor de A é {valorA}")
print(f"O valor de B é {valorB}\n")

valorGuardado = valorA
valorA = valorB
valorB = valorGuardado

print(f"Agora o valor de A é {valorA}")
print(f"Agora o valor de B é {valorB}")
