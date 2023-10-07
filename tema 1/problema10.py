def count_words(text):
    # Split the text into words using a single space as the separator
    words = text.split(" ")

    # Filter out empty strings (resulting from multiple spaces)
    words = [word for word in words if word.strip() != ""]

    # Return the count of words
    return len(words)


# Input text from the user
text = input("Enter a text: ")

# Call the function to count words
word_count = count_words(text)

print(f"The number of words in the text is: {word_count}")
