import random
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    try:
        # Ask the user for the desired password length
        while True:
            try:
                password_length = int(input("Enter the length of the password: "))
                if password_length <= 0:
                    print("Password length must be a positive integer.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

        # Ask the user if they want to include letters
        while True:
            include_letters = input("Include letters in the password? (y/n): ").lower()
            if include_letters == 'y':
                break
            elif include_letters == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        # Ask the user if they want to include numbers
        while True:
            include_numbers = input("Include numbers in the password? (y/n): ").lower()
            if include_numbers == 'y':
                break
            elif include_numbers == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        # Ask the user if they want to include symbols
        while True:
            include_symbols = input("Include symbols in the password? (y/n): ").lower()
            if include_symbols == 'y':
                break
            elif include_symbols == 'n':
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        # Generate the password if at least one type is included
        if include_letters == 'n' and include_numbers == 'n' and include_symbols == 'n':
            print("You must include at least one type of characters (letters, numbers, or symbols).")
        else:
            password = generate_password(password_length, include_letters == 'y', include_numbers == 'y', include_symbols == 'y')
            print("Generated Password:", password)

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")
        break
