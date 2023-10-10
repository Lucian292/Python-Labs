def find_unseen_seats(matrix: list[list[int]]) -> list[tuple[int, int]]:  # (row, col
    unseen_seats = []
    rows = len(matrix)
    cols = len(matrix[0])

    for row in range(rows):
        for col in range(cols):
            height = matrix[row][col]
            can_see = True

            # Check if there is a taller spectator in front
            for r in range(row + 1, rows):
                if matrix[r][col] > height:
                    can_see = False
                    break

            if not can_see:
                unseen_seats.append((row, col))

    return unseen_seats

stadium_matrix = [
    [1, 2, 3, 2, 1, 1],
    [2, 4, 4, 3, 7, 2],
    [5, 5, 2, 5, 6, 4],
    [6, 6, 7, 6, 7, 5]
]

unseen_seats = find_unseen_seats(stadium_matrix)
print(unseen_seats)
