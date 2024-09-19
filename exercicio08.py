nota1 = float(input("Digite 1º Nota: "))
nota2 = float(input("Digite 2º Nota: "))
nota3 = float(input("Digite 3º Nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"O aluno está aprovado!! com média: {media:.2f}")
else:
    if media >= 4:
        print(f"O aluno está em recuperação!! com média: {media:.2f}")
    else:
        print(f"O aluno está reprovado!! com média: {media:.2f}")
