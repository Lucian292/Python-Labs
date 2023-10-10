def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_primes_in_list(numbers: list[int]) -> list[int]:
    prime_numbers = []
    for num in numbers:
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers

input_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_result = find_primes_in_list(input_numbers)
print("Prime numbers in the list:", prime_result)
