import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7

print("🎯 Number Guessing Game")
print("Guess a number between 1 and 100")

while attempts < max_attempts:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Correct! You guessed it in {attempts} attempts.")
            break

    except ValueError:
        print("Please enter a valid number.")

if attempts == max_attempts and guess != secret_number:
    print(f"😢 Game Over! The number was {secret_number}")
