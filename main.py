try:
    print("1" + 1)
except TypeError:
    print("Erro de tipo")

try:
    lista = [0] * 5
    lista[10] = 1
except IndexError:
    print("Erro de index")

try:
    dicionario = {}
    print(dicionario['id'])
except KeyError:
    print("Erro  de chave")

try:
    x = 'aaaa'
    x.reverse()
except AttributeError:
    print("Erro de atributo")

try:
    print(int('a77'))
except ValueError:
    print("Erro de valor")
