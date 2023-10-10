def order_tuples_by_third_character(tuples_list: list[tuple]) -> list[tuple]:
    # Define a custom sorting key function
    def custom_key(item):
        # Check if the second element has at least three characters
        if len(item[1]) >= 3:
            # Return the third character of the second element
            return item[1][2]
        else:
            # If the second element has fewer than three characters, return an empty string
            return ''

    # Sort the list of tuples using the custom key function
    sorted_tuples = sorted(tuples_list, key=custom_key)

    return sorted_tuples

input_tuples = [('abc', 'bcd'), ('abc', 'zza')]
ordered_tuples = order_tuples_by_third_character(input_tuples)
print(ordered_tuples)
