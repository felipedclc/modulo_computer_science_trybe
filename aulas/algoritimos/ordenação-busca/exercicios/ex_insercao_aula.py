# Dado uma lista já ordenada, como decidir onde colocar um número a mais?
# quadrático O(n²) -> RUIM
# linear O(n) -> MEDIO
# binário O(n/2) -> BOM

entrada = [1, 3, 5, 7, 9, 11, 21, 23, 30, 42, 56]  # lista ordenada


def onde_inserir(numeros, numero):
    # função que será chamada - arr,  num, pos inicial, pos final
    return _onde_inserir(numeros, numero, 0, len(numeros) - 1)


def _onde_inserir(numeros, numero, inicial, final):
    if inicial == final:
        return inicial

    meio = (inicial + final) // 2
    if numero < numeros[meio]:
        return _onde_inserir(numeros, numero, inicial, meio)
    else:
        return _onde_inserir(numeros, numero, meio + 1, final)


print(onde_inserir(entrada, 12))
entrada.insert(onde_inserir(entrada, 12), 12)
print(entrada)
