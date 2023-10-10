def is_palindrome(num: int) -> bool:
    # Convert the number to a string for easier palindrome checking
    num_str = str(num)
    return num_str == num_str[::-1]

def find_palindromes(numbers: list[int]) -> tuple[int, int]:
    palindrome_count = 0
    greatest_palindrome = None

    for num in numbers:
        if is_palindrome(num):
            palindrome_count += 1
            if greatest_palindrome is None or num > greatest_palindrome:
                greatest_palindrome = num

    return (palindrome_count, greatest_palindrome)

# Example usage:
number_list = [121, 123, 1331, 45654, 78987, 1001]

result = find_palindromes(number_list)
print("Number of palindromes:", result[0])
print("Greatest palindrome:", result[1])
