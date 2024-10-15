from classe import Pessoa

pessoa:Pessoa = Pessoa('caio',65,24)
"""
Na anotação de tipo, ao criar um objeto, sua variável pode receber a anotação de tipo correspondente à classe do objeto.
A variável se torna do tipo Pessoa porque, ao atribuir uma instância da classe Pessoa a essa variável, você está 
essencialmente definindo que ela conterá um objeto que possui as características e comportamentos (métodos e atributos) 
definidos nessa classe.
"""
pessoa.nome = 'Caio Gabriel Marinho'
print(pessoa.nome)
pessoa.dormir()
pessoa.acordar()
pessoa.comer()