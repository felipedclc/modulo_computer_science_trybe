def sum_square_difference(n):
    quadrados_soma = []
    soma_quadrados = []
    for num in range(1, n + 1):
        quadrados_soma.append(num)
        soma_quadrados.append(num ** 2)

    return sum(quadrados_soma) ** 2 - sum(soma_quadrados)


print(sum_square_difference(10))
