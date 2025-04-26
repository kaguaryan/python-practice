def factorial(number):
    total = 1
    for i in range(1, number + 1):  # Multiply each number from 1 to the given number
        total *= i
    return total

print("The factorial of 7 is", factorial(7))
