from generator import generate_password

num_passwords = 5

password_length = 16
include_special_chars = True
include_numbers = True

for _ in range(num_passwords):
    password = generate_password(length=password_length, include_special_chars=include_special_chars, include_numbers=include_numbers)
    print(f"Generated Password: {password}")
