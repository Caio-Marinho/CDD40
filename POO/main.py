from dados import Pessoa,Espanhol

dado = Pessoa('caio',23)
print(f"{dado.nome()} tem {dado.idade()} anos")
dado.anivesario()
print(f"{dado.nome()} tem {dado.idade()} anos e {dado.falar()}")
dado.anivesario()
pessoa = Espanhol(dado.nome(),dado.idade())
print(f"{pessoa.nome()} tem {pessoa.idade()} anos e agora {pessoa.falar()}")