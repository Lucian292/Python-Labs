def count_set_bits(number):
    # Initialize a counter to keep track of set bits
    count = 0

    # Loop through each bit in the binary representation of the number
    while number > 0:
        # Check if the least significant bit (rightmost bit) is 1
        if number & 1:
            count += 1

        # Right-shift the number by 1 bit to process the next bit
        number >>= 1

    return count


# Input number from the user
number = int(input("Enter a number: "))

# Call the function to count set bits
bit_count = count_set_bits(number)

print(f"The number of set bits in {number} is: {bit_count}")
