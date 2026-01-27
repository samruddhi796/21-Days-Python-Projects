import time
import json
import os
from datetime import datetime

SESSION_FILE = "sessions.json"
WORK_TIME = 25 * 60      # 25 minutes
BREAK_TIME = 5 * 60      # 5 minutes


def load_sessions():
    if not os.path.exists(SESSION_FILE):
        return []
    with open(SESSION_FILE, "r") as file:
        return json.load(file)


def save_sessions(sessions):
    with open(SESSION_FILE, "w") as file:
        json.dump(sessions, file, indent=4)


def countdown(seconds, label):
    while seconds:
        mins, secs = divmod(seconds, 60)
        print(f"\r{label} Time Left: {mins:02}:{secs:02}", end="")
        time.sleep(1)
        seconds -= 1
    print()


def record_session(sessions):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "time": datetime.now().strftime("%H:%M"),
        "type": "Work"
    }
    sessions.append(entry)
    save_sessions(sessions)


def show_stats(sessions):
    today = datetime.now().strftime("%Y-%m-%d")
    today_sessions = [s for s in sessions if s["date"] == today]

    print("\n📊 Today’s Pomodoro Stats")
    print(f"Completed Pomodoros: {len(today_sessions)}")


def start_pomodoro():
    sessions = load_sessions()

    print("\n🍅 Pomodoro Started — Focus!")
    countdown(WORK_TIME, "Work")

    record_session(sessions)
    print("\n✅ Work session complete!")

    print("\n☕ Break Time")
    countdown(BREAK_TIME, "Break")

    show_stats(sessions)


def menu():
    print("\n🍅 Pomodoro Timer")
    print("1. Start Pomodoro")
    print("2. View Today’s Stats")
    print("3. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            start_pomodoro()
        elif choice == '2':
            sessions = load_sessions()
            show_stats(sessions)
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
