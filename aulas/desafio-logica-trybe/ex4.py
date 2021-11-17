def multiples_of_3_or_5(roof):
    nums = []
    for i in range(roof - 1):
        nums.append(i + 1)

    sum_multiples = 0
    for num in nums:
        if num % 3 == 0 or num % 5 == 0:
            sum_multiples += num
    return sum_multiples


print(multiples_of_3_or_5(10))
