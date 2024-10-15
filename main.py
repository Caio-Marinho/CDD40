from classe import *

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

animal = Animal('bx','preta')
animal.comer()

gato = Gato("Frajola","Preto")
gato.comer()
gato.miar()

cachorro = Cachorro('rex','Preta')
cachorro.latir()
cachorro.comer()

vaca = Vaca("mimosa","Preta")
vaca.comer()
vaca.mugir()

coelho = Coelho("Algodão","Branco")
coelho.comer()
coelho.grunir()

tri = TriAtleta('Caio',65)
tri.aposetar()
tri.aquecer()
tri.correr()
tri.pararCorrer()
tri.pedalar()
tri.pararPedalar()
tri.nadar()
tri.pararNadar()