import requests
import json
import os

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"
FAVORITES_FILE = "favorites.json"


def fetch_rates():
    try:
        response = requests.get(API_URL, timeout=5)
        response.raise_for_status()
        data = response.json()
        return data["rates"]
    except requests.RequestException:
        print("❌ Error fetching exchange rates.")
        return None


def load_favorites():
    if not os.path.exists(FAVORITES_FILE):
        return []

    with open(FAVORITES_FILE, "r") as file:
        return json.load(file)


def save_favorites(favorites):
    with open(FAVORITES_FILE, "w") as file:
        json.dump(favorites, file, indent=4)


def convert_currency(rates):
    from_currency = input("From currency (e.g. USD): ").upper()
    to_currency = input("To currency (e.g. INR): ").upper()

    if from_currency not in rates or to_currency not in rates:
        print("❌ Invalid currency code.")
        return

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("❌ Invalid amount.")
        return

    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]

    print(f"✅ {amount} {from_currency} = {converted:.2f} {to_currency}")

    save = input("Save this conversion? (y/n): ")
    if save.lower() == 'y':
        favorites = load_favorites()
        favorites.append({
            "from": from_currency,
            "to": to_currency,
            "amount": amount,
            "result": round(converted, 2)
        })
        save_favorites(favorites)
        print("⭐ Saved to favorites.")


def view_favorites():
    favorites = load_favorites()
    if not favorites:
        print("📭 No saved conversions.")
        return

    for fav in favorites:
        print(f"{fav['amount']} {fav['from']} → {fav['result']} {fav['to']}")


def menu():
    print("\n💱 Currency Converter")
    print("1. Convert Currency")
    print("2. View Favorites")
    print("3. Exit")


def main():
    rates = fetch_rates()
    if not rates:
        return

    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            convert_currency(rates)
        elif choice == '2':
            view_favorites()
        elif choice == '3':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice.")


main()
