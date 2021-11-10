# Dado uma coleção de números inteiros ordenados em ordem crescente,
# tem um inteiro que aparce mais que 25% das vezes

# Analise a ordem de complexidade de tempo e espaço.

from typing import Counter


test_1 = [1, 2, 2, 6, 6, 6, 6, 7, 10]


dict_numb = Counter(test_1)
for numb, count in dict_numb.items():
    numb_25 = None
    if count > (len(test_1) / 4):
        numb_25 = numb
        print(numb_25)


# forma prof - pegar os numeros de 4 em 4(ordenado)
def more_than_25_percent(array):
    # percent_25 = len(array) // 4
    percent_75 = len(array) - len(array) // 4
    print(percent_75)
    for index, element in enumerate(array):
        print(index, element)

    return None


more_than_25_percent(test_1)
