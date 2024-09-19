"""programa para ler o nome de uma
pessoa, a sua idade e o seu salário e mostre
essas informações na tela."""
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
salario = float(input("Informe o salario: "))

print(f"{nome} tem {idade} anos e ganha R$ {salario+salario*0.1}")
aumento = salario+salario*0.1
meses = idade*12
print(f"nome           | {nome}")
print("__________________")
print(f"Idade          | {idade}")
print("___________________")
print(f"Mês de vida    | {meses}")
print("___________________")
print(f"salario        | {aumento:,.2f}")
