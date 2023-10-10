def compose(musical_notes: list, moves: list, start_position: int) -> list[str]:
    song = []
    current_position = start_position

    for move in moves:
        current_position += move
        # Ensure the current position is within bounds
        current_position %= len(musical_notes)

        song.append(musical_notes[current_position])

    return song

# Example usage:
notes = ["do", "re", "mi", "fa", "sol"]
moves = [1, -3, 4, 2]
start_position = 2

result = compose(notes, moves, start_position)
print(result)
