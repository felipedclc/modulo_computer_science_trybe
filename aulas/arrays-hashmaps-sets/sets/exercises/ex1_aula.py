def cartas_faltantes(minhas_cartas):
    return set(range(1, 21)) - set(minhas_cartas)


if __name__ == "__main__":
    minhas_cartas = [1, 2, 2, 3, 4, 5, 6, 7, 8, 11]
    print(cartas_faltantes(minhas_cartas))
    # print([i for i in range(1, 21)])
