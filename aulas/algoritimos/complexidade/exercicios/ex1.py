def contains_duplicate(numbers):
    numbers.sort()
    previous_number = "not a number"
    for number in numbers:
        if previous_number == number:
            return True
        previous_number = number

    return False


print(contains_duplicate([1, 2, 3, 3, 4]))


# O algoritmo faz uma iteração para cada elemento do array de entrada,
# o numbers, então, tendo n como o tamanho da entrada o algoritmo tem
# uma Complexidade de Tempo O(n).
# O que ele faz a cada iteração, no entanto, é alterar o valor de uma
# variável, a result. Sendo assim, tenha a entrada um ou cem mil elementos,
# o espaço em memória ocupado será o mesmo. Assim sendo, a
# Complexidade de Espaço do algoritmo é O(1)
