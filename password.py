import random
import string

def generate_password(length, use_numbers, use_symbols):
    characters = string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        # Ask the user for the desired password length
        password_length = int(input("Enter the length of the password: "))

        # Ask the user if they want to include numbers
        include_numbers = input("Include numbers in the password? (y/n): ").lower() == 'y'

        # Ask the user if they want to include symbols
        include_symbols = input("Include symbols in the password? (y/n): ").lower() == 'y'

        # Generate the password
        password = generate_password(password_length, include_numbers, include_symbols)
        print("Generated Password:", password)

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break
