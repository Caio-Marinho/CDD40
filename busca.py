def busca_binaria(lista: list[int], valor: int) -> int:
    """Buscador binario vai fazer uma busca pela lista ordenada separando pela metade da lista
    procurando valor compatível.
    Args:
        Lista: lista dos números,
        Valor: a ser buscodo
    return:
        retorna -1 caso não seja encontrado o valor e a posição caso seja enccontrado."""
    esquerda = 0
    direita = len(lista) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        # Verifica se o valor está no meio
        if lista[meio] == valor:
            return meio
        # Se o valor é maior, ignora a metade esquerda
        elif lista[meio] < valor:
            esquerda = meio + 1
        # Se o valor é menor, ignora a metade direita
        else:
            direita = meio - 1

    return -1  # Retorna -1 se o valor não for encontrado


def ordenador(lista: list[int]) -> list[int]:
    """Ordenador de lista que vai ordenar a lista do menor para o maior
    pelo bubble sort
    Args:
        Recebe lista
    return
        retorna a lista"""
    tamanhoLista = len(lista)  # tamanho da lista
    for i in range(tamanhoLista):
        for j in range(tamanhoLista - 1):  # percorre a lista verificando todos os itens em todas as posições
            if lista[j] > lista[j + 1]:  # verifica se o item na posição x é maior que o dá x+1
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # troca o item da posição x como dá x+1
    return lista  # retorna lista ordenada


# Exemplo de uso
lista = [13, 7, 1, 17, 9, 20, 3, 15, 5, 11]
lista_ordenada = ordenador(lista.copy())  # copia da variável lista para manter a original intacta
valor_procurado = 7
print(lista)
resultado = busca_binaria(lista_ordenada, valor_procurado)

if resultado != -1:
    print(f"Valor {valor_procurado} encontrado na posição {resultado}.")
else:
    print(f"Valor {valor_procurado} não encontrado na lista.")