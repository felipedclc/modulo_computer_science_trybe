# from collections import Counter
import statistics


class Estatistica:
    @classmethod
    def media(cls, numbers):
        return sum(numbers) / len(numbers)

    @classmethod
    def mediana(cls, numbers):
        sort_numbers = sorted(numbers)  # numbers.sort() -> apenas ordena
        if len(sort_numbers) % 2 != 0:
            meio = len(sort_numbers) // 2 + 1
            return sort_numbers[meio]
        else:
            meio1 = len(sort_numbers) // 2 + 1
            meio2 = len(sort_numbers) // 2
            return (sort_numbers[meio1] + sort_numbers[meio2]) / 2

    @classmethod
    def moda(cls, numbers):
        return statistics.multimode(numbers)


# testando função:
def mediana(numbers):
    sort_numbers = sorted(numbers)  # numbers.sort()
    print(sort_numbers)
    if len(sort_numbers) % 2 != 0:
        meio = len(sort_numbers) // 2
        print(f"meio = {sort_numbers[meio]}")
        return sort_numbers[meio]
    else:
        meio1 = len(sort_numbers) // 2 - 1  # porque index começa no 0
        meio2 = len(sort_numbers) // 2
        return (sort_numbers[meio1] + sort_numbers[meio2]) / 2


print(mediana([1, 4, 6, 10, 11, 2]))
print(statistics.median([1, 4, 6, 10, 11, 2]))

# 5 // 2 = 2 -> divisão que retorna o inteiro arredondado p baixo
