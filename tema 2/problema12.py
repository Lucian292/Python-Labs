def group_by_rhyme(words: list) -> list:
    # Create an empty dictionary to store words grouped by their rhymes
    rhyme_groups = {}

    # Iterate through the words
    for word in words:
        # Get the last two letters of the word
        rhyme = word[-2:]

        # Check if the rhyme is already in the dictionary
        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            rhyme_groups[rhyme] = [word]

    # Convert the dictionary values to a list of lists
    grouped_words = list(rhyme_groups.values())

    return grouped_words

words_list = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words_list)
print(result)
# am schimbat branchul default