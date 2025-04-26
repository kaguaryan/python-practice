number = 189820
def sum_of_digits(number):
    sum = 0  # Initialize total_sum to 0
    while number > 0:  # Runs until they're no digits left in that number
        sum += number % 10  # Add the last digit to sum
        number = number // 10  # Remove the last digit from the number
    return sum  # Return the sum of the digits

print(sum_of_digits(189820))  # Calculate and print the sum of digits of 189820
