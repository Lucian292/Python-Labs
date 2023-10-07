# Function to count vowels in a string
def count_vowels(input_string):
    vowels = "aeiouAEIOU"  # List of vowels
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1

    return vowel_count

# Read a string from the console
input_string = input("Enter a string: ")

# Calculate the number of vowels in the string
num_vowels = count_vowels(input_string)

# Display the result
print(f"Number of vowels in the string: {num_vowels}")
