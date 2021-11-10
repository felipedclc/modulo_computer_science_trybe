# Dado um número inteiro positivo decimal, crie uma função recursiva
# que converta sua base para binária.


def convert(numb):
    result, rest = divmod(numb, 2)
    if numb > 1:
        convert(result)
    print(rest, end="")


convert(10)
