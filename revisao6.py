peso = float(input("Informe seu peso: "))
altura = float(input("Informe seu altura: "))
imc = peso/(altura ** 2)
if imc <=18.5:
    print(f"Seu IMC é {imc:.2f} então está abaixo do peso")
elif 18.6<=imc and imc < 25:
    print(f"Seu IMC é {imc:.2f} então está no peso ideal, parabens!!")
elif 25<= imc and imc < 30 :
    print(f"Seu IMC é {imc:.2f} então Levemente acima do peso")
elif 30<=imc and imc<35:
    print(f"Seu IMC é {imc:2f} então está com obesidade grau I")
elif 35<=imc and imc<40:
    print(f"Seu IMC é {imc:.2f} então Obsidade grau II(severa)")
else:
    print(f"Seu IMC é {imc:.2f} então Obsidade grau III(mórbida)")