import random


# resolução course ---------------------------------------------------------

def randomAverages(n):
    list_of_averages = []

    for _ in range(100):
        average = 0
        for _ in range(n):
            average += random.randrange(1, n)
        average = average / n
        list_of_averages.append(average)

    return list_of_averages


print(randomAverages(9))


# resolução autoral ---------------------------------------------------------

def generate_random_numbers(len):
    array_random_numbers = []
    for index in range(len):
        crazy_number = random.randint(1, 9)
        array_random_numbers.append(crazy_number)
    return array_random_numbers


def calculate_average(array):
    sum_numbers = sum(array)
    return sum_numbers / len(array)


def generate_random_array():
    array_random_numbers = []
    for index in range(100):
        random_numbers = generate_random_numbers(10)
        average_random_number = calculate_average(random_numbers)
        array_random_numbers.append(average_random_number)
    return array_random_numbers


# array_numbers = generate_random_numbers(10)
# print(array_numbers)
# print(calculate_average(array_numbers))
print(generate_random_array())
