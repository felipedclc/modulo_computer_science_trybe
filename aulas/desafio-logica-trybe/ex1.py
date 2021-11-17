#!/bin/python3

# Complete the 'fahrenheit_to_celsius' function below.
# The function is expected to return a FLOAT.
# The function accepts INTEGER temp_fahrenheit as parameter.


def fahrenheit_to_celsius(temp_fahrenheit):
    return (temp_fahrenheit - 32) / 1.8


if __name__ == "__main__":
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    fptr = 95

    result = fahrenheit_to_celsius(fptr)

    print(result)
