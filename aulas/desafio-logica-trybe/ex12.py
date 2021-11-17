def is_palindromo(number):
    crazy_loop = 0
    sum = 0
    normal = str(number)
    inverse = str(number)[::-1]

    if normal == inverse:
        int(normal) + int(inverse)
        return normal
    else:
        sum = int(normal) + int(inverse)
        crazy_loop += 1
        print("xablau", crazy_loop)
        return is_palindromo(sum)


print(is_palindromo(349))
print(sum(212))
