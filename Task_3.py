
import random
import string

while True:

    try:
        # Password length
        length = int(input("Enter password length (minimum 8): "))

        if length < 8:
            raise ValueError("Password length must be at least 8")

        # Character type options
        print("\nChoose character types:")
        print("1. Uppercase letters")
        print("2. Lowercase letters")
        print("3. Numbers")
        print("4. Symbols")

        choices = input("Enter your choices (example: 1,2,3): ")
        choices = choices.split(",")

        # Remove spaces
        choices = [choice.strip() for choice in choices]

        # Check at least 2 types
        if len(set(choices)) < 2:
            raise ValueError("Select at least 2 character types")

        # Character pool
        characters = ""

        if "1" in choices:
            characters += string.ascii_uppercase

        if "2" in choices:
            characters += string.ascii_lowercase

        if "3" in choices:
            characters += string.digits

        if "4" in choices:
            characters += string.punctuation

        # Check invalid choices
        if not all(choice in ["1", "2", "3", "4"] for choice in choices):
            raise ValueError("Invalid character type selected")

        # Generate password
        password = ""

        for i in range(length):
            password += random.choice(characters)

        print("\nGenerated Password:", password)

    except ValueError as e:
        print("Error:", e)

    # Generate another password
    again = input("\nGenerate another password? (y/n): ")

    if again.lower() != "y":
        print("Program ended.")
        break