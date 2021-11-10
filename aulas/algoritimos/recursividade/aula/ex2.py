# Dado uma lista de inteiros, crie uma função que inverta a posição
# dos seus elementos, sem utilizar for ou while

list_numbers = [40, 42, 9, 17, 15, 25]  # [25, 15, 17, 9, 42, 40]


def inversao(list):
    if len(list) == 0:
        return list
    print("lista:", list)
    resultado = inversao(list[: len(list) - 1])
    print("result:", resultado)
    return [list[-1]] + resultado


print(inversao(list_numbers))
# print(list)
