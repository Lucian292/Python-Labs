# Function to count occurrences of a substring in a string
def count_occurrences(main_string, sub_string):
    count = 0
    start = 0

    while start < len(main_string):
        start = main_string.find(sub_string, start)
        if start == -1:
            break
        count += 1
        start += 1

    return count

# Read two strings from the console
string1 = input("first string: ")
string2 = input("second string: ")

# Calculate the number of occurrences
occurrences = count_occurrences(string1, string2)

# Display the result
print(f"The string '{string2}' occurs {occurrences} times in '{string1}'.")
