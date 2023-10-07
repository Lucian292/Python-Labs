def spiral_order(matrix):
    result = []
    while matrix:
        result += matrix[0]  # Add the first row to the result
        matrix = list(zip(*matrix[1:]))[::-1]  # Rotate the remaining matrix counterclockwise
    return ''.join(result)

# Input matrix dimensions from the user
n = int(input("number of rows: "))
m = int(input("number of columns: "))

# Input matrix elements from the user
matrix = []
for i in range(n):
    row = input(f"Enter row {i + 1} (use spaces between characters): ").split()
    matrix.append(row)

result = spiral_order(matrix)
print(result)
