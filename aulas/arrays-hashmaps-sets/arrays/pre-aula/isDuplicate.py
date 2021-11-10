test1 = [1, 2, 3, 1]  # saída True
test2 = []  # saída False
test3 = [1, 2, 3, 4]  # saída False
test4 = [1, 1, 1, 3, 3, 4, 4, 2, 1]  # saída True


def isDuplicate(list):
    list.sort()  # ordenar antes para verificação
    for index in range(len(list) - 1):
        if list[index] == list[index + 1]:
            return True
    return False


print(isDuplicate(test1))
print(isDuplicate(test2))
print(isDuplicate(test3))
print(isDuplicate(test4))
