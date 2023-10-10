def replace_below_main_diagonal_with_zeros(matrix: list) -> list:
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix with the same dimensions, initialized to zeros
    result_matrix = [[0] * num_cols for _ in range(num_rows)]

    # Copy the elements from the original matrix to the result_matrix,
    # but replace elements below the main diagonal with zeros
    for i in range(num_rows):
        for j in range(num_cols):
            if i <= j:  # Elements on or above the main diagonal
                result_matrix[i][j] = matrix[i][j]

    return result_matrix

matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 10],
    [10, 11, 12, 13]
]

result = replace_below_main_diagonal_with_zeros(matrix)
for row in result:
    print(row)
