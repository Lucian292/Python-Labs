from operations import add, subtract, multiply, divide

# Integer operations
result_add_int = add(5, 3)
result_subtract_int = subtract(8, 4)
result_multiply_int = multiply(2, 6)
result_divide_int = divide(10, 2)

print(f"Integer Addition: {result_add_int}")
print(f"Integer Subtraction: {result_subtract_int}")
print(f"Integer Multiplication: {result_multiply_int}")
print(f"Integer Division: {result_divide_int}")

# Floating-point operations
result_add_float = add(5.0, 3.5)
result_subtract_float = subtract(8.7, 4.2)
result_multiply_float = multiply(2.5, 6.0)
result_divide_float = divide(10.0, 2.0)

print(f"Floating-point Addition: {result_add_float}")
print(f"Floating-point Subtraction: {result_subtract_float}")
print(f"Floating-point Multiplication: {result_multiply_float}")
print(f"Floating-point Division: {result_divide_float}")
