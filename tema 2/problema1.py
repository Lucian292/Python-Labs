def generate_fibonacci(n: int) -> list[int]:
    fibonacci_sequence = []
    a, b = 0, 1

    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b

    return fibonacci_sequence

n = int(input("Enter the value of n: "))

result = generate_fibonacci(n)

print(result)
