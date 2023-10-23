def count_characters(text):
    character_count = {}

    for char in text:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1

    return character_count

input_text = "Ana has apples."
result = count_characters(input_text)
print(result)
