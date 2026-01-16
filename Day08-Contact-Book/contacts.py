import csv
import os

FILE_NAME = "contacts.csv"


def load_contacts():
    contacts = []
    if not os.path.exists(FILE_NAME):
        return contacts

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)

    return contacts


def save_contacts(contacts):
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["name", "phone", "email"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email
    })

    save_contacts(contacts)
    print("✅ Contact added.")


def view_contacts(contacts):
    if not contacts:
        print("📭 No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | {contact['phone']} | {contact['email']}")


def search_contact(contacts):
    keyword = input("Search name: ").lower()
    found = False

    for contact in contacts:
        if keyword in contact["name"].lower():
            print(f"{contact['name']} | {contact['phone']} | {contact['email']}")
            found = True

    if not found:
        print("❌ No matching contact.")


def delete_contact(contacts):
    view_contacts(contacts)
    index = int(input("Enter contact number to delete: ")) - 1

    if 0 <= index < len(contacts):
        removed = contacts.pop(index)
        save_contacts(contacts)
        print(f"🗑 Deleted {removed['name']}")
    else:
        print("❌ Invalid selection.")


def menu():
    print("\n📇 CONTACT BOOK")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    contacts = load_contacts()

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
