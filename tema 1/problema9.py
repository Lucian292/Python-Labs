def most_common_letter(text):
    # Convert the text to lowercase to ignore casing
    text = text.lower()

    # Create a dictionary to store the count of each letter
    letter_count = {}

    # Iterate through the characters in the text
    for char in text:
        # Check if the character is a letter (A-Z or a-z)
        if char.isalpha():
            # Update the count for the letter in the dictionary
            if char in letter_count:
                letter_count[char] += 1
            else:
                letter_count[char] = 1

    # Find the letter with the highest count
    most_common = max(letter_count, key=letter_count.get)

    return most_common, letter_count[most_common]


# Input text from the user
text = input("Enter a text: ")

# Call the function to find the most common letter
common_letter, count = most_common_letter(text)

print(f"The most common letter is '{common_letter}' with {count} occurrences.")
