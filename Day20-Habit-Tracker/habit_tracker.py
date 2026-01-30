import json
import os
from datetime import datetime, timedelta

FILE_NAME = "habits.json"


def load_habits():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_habits(habits):
    with open(FILE_NAME, "w") as file:
        json.dump(habits, file, indent=4)


def add_habit(habits):
    name = input("Enter habit name: ").strip()

    if name in habits:
        print("❌ Habit already exists.")
        return

    habits[name] = {
        "dates": [],
        "streak": 0,
        "longest_streak": 0
    }

    save_habits(habits)
    print("✅ Habit added.")


def update_streak(dates):
    if not dates:
        return 0, 0

    dates = sorted(datetime.strptime(d, "%Y-%m-%d") for d in dates)

    longest = current = 1

    for i in range(1, len(dates)):
        if dates[i] - dates[i - 1] == timedelta(days=1):
            current += 1
            longest = max(longest, current)
        else:
            current = 1

    return current, longest


def mark_complete(habits):
    today = datetime.today().strftime("%Y-%m-%d")

    name = input("Enter habit name: ")

    if name not in habits:
        print("❌ Habit not found.")
        return

    if today in habits[name]["dates"]:
        print("ℹ Habit already marked for today.")
        return

    habits[name]["dates"].append(today)

    streak, longest = update_streak(habits[name]["dates"])
    habits[name]["streak"] = streak
    habits[name]["longest_streak"] = max(
        habits[name]["longest_streak"], longest
    )

    save_habits(habits)
    print("🔥 Habit marked complete for today!")


def view_habits(habits):
    if not habits:
        print("📭 No habits found.")
        return

    print("\n📋 HABITS")
    for name, data in habits.items():
        print(
            f"- {name} | Current Streak: {data['streak']} | Longest: {data['longest_streak']}"
        )


def show_calendar(habits):
    name = input("Enter habit name: ")
    if name not in habits:
        print("❌ Habit not found.")
        return

    today = datetime.today()
    start = today.replace(day=1)
    dates_done = set(habits[name]["dates"])

    print(f"\n📆 {name} — {today.strftime('%B %Y')}")
    print("Mo Tu We Th Fr Sa Su")

    day = start - timedelta(days=start.weekday())
    for _ in range(42):  # 6 weeks view
        date_str = day.strftime("%Y-%m-%d")
        symbol = "✔" if date_str in dates_done else "·"

        print(f"{symbol} ", end="")

        if day.weekday() == 6:
            print()
        day += timedelta(days=1)

    print()


def stats(habits):
    total_days = 0
    completed_days = 0

    for data in habits.values():
        completed_days += len(data["dates"])
        total_days += 30  # approx monthly

    if total_days == 0:
        print("📊 No data.")
        return

    rate = (completed_days / total_days) * 100
    print(f"📊 Completion Rate: {rate:.2f}%")


def menu():
    print("\n📅 Habit Tracker")
    print("1. Add Habit")
    print("2. Mark Habit Complete")
    print("3. View Habits")
    print("4. View Monthly Calendar")
    print("5. View Stats")
    print("6. Exit")


def main():
    habits = load_habits()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_habit(habits)
        elif choice == '2':
            mark_complete(habits)
        elif choice == '3':
            view_habits(habits)
        elif choice == '4':
            show_calendar(habits)
        elif choice == '5':
            stats(habits)
        elif choice == '6':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
