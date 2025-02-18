import math

# Function to check if a number is a perfect square
def is_perfect_square(number):
    sqrt_value = math.sqrt(number)
    return sqrt_value.is_integer()

# Test the function
input_number = int(input("Enter a number: "))

if is_perfect_square(input_number):
    print(f"{input_number} is a perfect square.")
else:
    print(f"{input_number} is not a perfect square.")
