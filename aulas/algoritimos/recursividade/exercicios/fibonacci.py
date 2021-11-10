def fibonacci(n):
    prev = 1
    arr = [0]
    for i in range(n - 1):
        arr[i] += prev
        arr.append(arr[i])
        prev = arr[i - 1]

    arr.insert(0, 0)
    arr.insert(1, 1)
    arr.pop(len(arr) - 1)
    print(arr)
    return arr[n - 1]


print(fibonacci(9))

# Python program to display the Fibonacci sequence ---------------------


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)


print(recur_fibo(9))

nterms = 10

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nterms):
        print(recur_fibo(i))
