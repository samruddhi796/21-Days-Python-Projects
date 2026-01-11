# simple calculater with history

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b    

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b    

history = []

print("Welcome to the Calculator!")
print("Available operations: add, subtract, multiply, divide, power, modulus")
print("Type 'q' anytime to quit\n")

while True:
    user_input = input("Enter first number (or 'q' to quit): ")
    if user_input.lower() == 'q':
        break
    try:
        num1 = float(user_input)
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.\n")
        continue

    operator = input("Choose operation (+, -, *, /, **, %): ")

    if operator == '+':
        result = add(num1, num2)
    elif operator == '-':
        result = subtract(num1, num2)
    elif operator == '*':
        result = multiply(num1, num2)
    elif operator == '/':
        result = divide(num1, num2)
    elif operator == '**':
        result = power(num1, num2)
    elif operator == '%':
        result = modulus(num1, num2)
    else:
        print("Invalid operation.\n")
        continue

    print(f"Result: {result}\n")

# Save to history
    history.append(f"{num1} {operator} {num2} = {result}")

    show_history = input("Show history? (y/n): ")
    if show_history.lower() == 'y':
        print("\n--- Calculation History ---")
        for item in history:
            print(item)
        print()
print("Thank you for using the calculator. Goodbye!")