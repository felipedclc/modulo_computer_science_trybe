def even_fibonacci_numbers(roof):
    fibonacci = [1, 2]
    sum_evens = 2
    for index in range(roof):
        sum = fibonacci[index] + fibonacci[index + 1]
        fibonacci.append(sum)
        if sum % 2 == 0 and sum < 100:
            sum_evens += sum

    return sum_evens


print(even_fibonacci_numbers(10))
