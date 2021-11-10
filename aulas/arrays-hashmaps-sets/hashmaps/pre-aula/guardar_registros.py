# Encontre o número mais frequente, se houver empate retorne qualquer um

from typing import Counter


nums = [3, 2, 5, 4, 1, 2, 3, 1, 3, 4, 1]

# hash = {}


def numeros_repetidos(nums):
    count = {}
    most_frequent = nums[0]
    for num in nums:
        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

        if count[num] > count[most_frequent]:
            most_frequent = count[num]

    return most_frequent


print(numeros_repetidos(nums))


def numeros_repetidos_felipe(nums):
    count_nums = Counter(nums)

    max_num = nums[0]
    max_rep = 0
    for num, rep in count_nums.items():
        if rep > max_rep:
            max_rep = rep
            max_num = num
    return max_num


print(numeros_repetidos_felipe(nums))
