import random
import string

print("Password Generator")

# Character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

while True:
    try:
        length = int(input("\nEnter password length: "))
        if length <= 0:
            print("Length must be greater than 0.")
            continue
    except ValueError:
        print("Please enter a valid number.")
        continue

    print("\nChoose password type:")
    print("1. Memorable (letters only)")
    print("2. Strong (letters + numbers + symbols)")

    choice = input("Enter choice (1 or 2): ")

    if choice == '1':
        characters = letters
    elif choice == '2':
        characters = letters + digits + symbols
    else:
        print("Invalid choice.")
        continue

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))

    print(f"\nGenerated Password: {password}")

    again = input("\nGenerate another password? (y/n): ")
    if again.lower() != 'y':
        print("\nPassword Generator closed.")
        break
