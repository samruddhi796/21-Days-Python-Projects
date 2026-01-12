import json
import os

FILE_NAME = "tasks.json"


def load_tasks():
    # If file does not exist, return empty list
    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(tasks):
    title = input("Enter task: ")
    task_id = len(tasks) + 1

    task = {
        "id": task_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)
    print("✅ Task added.")


def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks found.")
        return

    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        print(f'{task["id"]}. {task["title"]} [{status}]')


def complete_task(tasks):
    task_id = int(input("Enter task ID to mark complete: "))

    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print("✅ Task marked as completed.")
            return

    print("❌ Task not found.")


def delete_task(tasks):
    task_id = int(input("Enter task ID to delete: "))

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print("🗑 Task deleted.")
            return

    print("❌ Task not found.")


def menu():
    print("\n📋 TO-DO LIST MENU")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit")


def main():
    tasks = load_tasks()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
