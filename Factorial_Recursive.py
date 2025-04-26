def factorial_recursive(number):
    if number == 1:  # Base case as factorial of 1 is 1
        return 1
    else:
        return number * factorial_recursive(number - 1)  # Recursive case

print(f"The factorial of 7 is {factorial_recursive(7)}")  # Print the factorial of 7
