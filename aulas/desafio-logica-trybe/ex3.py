def count_down(x):
    regress = []
    for i in reversed(range(x + 1)):
        regress.append(str(i))
    return "...".join(regress) + "!!!"


print(count_down(10))
