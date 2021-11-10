# crie uma função recursiva que faça uma contagem regressiva


def count(n):
    if n == 0:
        print("BOOM")
    else:
        # n - 1
        print(n)
        count(n - 1)


print(count(10))
