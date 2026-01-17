import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount.")
        return

    category = input("Enter category: ")

    date_input = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
    if date_input == "":
        date = datetime.today().strftime("%Y-%m-%d")
    else:
        try:
            datetime.strptime(date_input, "%Y-%m-%d")
            date = date_input
        except ValueError:
            print("❌ Invalid date format.")
            return

    expense = {
        "amount": amount,
        "category": category,
        "date": date
    }

    expenses.append(expense)
    save_expenses(expenses)
    print("✅ Expense added.")


def view_expenses(expenses):
    if not expenses:
        print("📭 No expenses recorded.")
        return

    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['date']} | {exp['category']} | ₹{exp['amount']}")


def filter_by_category(expenses):
    cat = input("Enter category: ").lower()
    filtered = [e for e in expenses if e["category"].lower() == cat]

    if not filtered:
        print("❌ No expenses found.")
        return

    for exp in filtered:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']}")


def filter_by_date(expenses):
    start = input("Start date (YYYY-MM-DD): ")
    end = input("End date (YYYY-MM-DD): ")

    try:
        start_date = datetime.strptime(start, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format.")
        return

    filtered = []
    for exp in expenses:
        exp_date = datetime.strptime(exp["date"], "%Y-%m-%d")
        if start_date <= exp_date <= end_date:
            filtered.append(exp)

    for exp in filtered:
        print(f"{exp['date']} | {exp['category']} | ₹{exp['amount']}")


def total_spending(expenses):
    total = sum(exp["amount"] for exp in expenses)
    print(f"💰 Total Spending: ₹{total}")


def menu():
    print("\n💸 EXPENSE TRACKER")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Filter by Category")
    print("4. Filter by Date Range")
    print("5. Show Total Spending")
    print("6. Exit")


def main():
    expenses = load_expenses()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_expense(expenses)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            filter_by_category(expenses)
        elif choice == '4':
            filter_by_date(expenses)
        elif choice == '5':
            total_spending(expenses)
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
