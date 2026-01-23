import json
import os
from datetime import datetime

FILE_NAME = "bmi_history.json"


def load_history():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_history(history):
    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def add_entry(history):
    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (meters): "))
    except ValueError:
        print("❌ Invalid input.")
        return

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "weight": weight,
        "height": height,
        "bmi": round(bmi, 2),
        "category": category
    }

    history.append(entry)
    save_history(history)

    print(f"✅ BMI: {entry['bmi']} ({category})")


def view_history(history):
    if not history:
        print("📭 No BMI history found.")
        return

    print("\n📊 BMI HISTORY")
    for entry in history:
        print(
            f"{entry['date']} | BMI: {entry['bmi']} | {entry['category']}"
        )


def menu():
    print("\n⚖ BMI Calculator")
    print("1. Calculate BMI")
    print("2. View BMI History")
    print("3. Exit")


def main():
    history = load_history()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_entry(history)
        elif choice == '2':
            view_history(history)
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
