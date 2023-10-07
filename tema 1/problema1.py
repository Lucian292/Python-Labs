import math

# Read numbers from the console
input_numbers = input("Enter multiple numbers separated by spaces: ")

# Convert input string into a list of integers
numbers = [int(x) for x in input_numbers.split()]

# Calculate the GCD
gcd = math.gcd(*numbers)

print(f"The greatest common divisor (GCD) of {numbers} is {gcd}")
