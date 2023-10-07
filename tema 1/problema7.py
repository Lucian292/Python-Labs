import re


def extract_number(text):
    # Use regular expression to find the first number in the text
    match = re.search(r'\d+', text)

    if match:
        # Extract and return the matched number as an integer
        return int(match.group())
    else:
        # Return None if no number is found in the text
        return None


# Input text from the user
text = input("Enter a text: ")

# Call the function to extract the first number
number = extract_number(text)

if number is not None:
    print(f"The first number in the text is: {number}")
else:
    print("No number found in the text.")
