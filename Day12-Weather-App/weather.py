import requests
import json
import os

API_KEY = "214cf972fa4833b4c640abca65f0d9ab"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}"
FAVORITES_FILE = "favorites.json"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        print("❌ Unable to fetch weather data.")
        return None

def display_weather(data):
    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\n🌤 Weather Information")
    print(f"Temperature: {temp}°C")
    print(f"Feels Like: {feels_like}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {condition.capitalize()}")


def load_favorites():
    if not os.path.exists(FAVORITES_FILE):
        return []

    with open(FAVORITES_FILE, "r") as file:
        return json.load(file)


def save_favorites(favorites):
    with open(FAVORITES_FILE, "w") as file:
        json.dump(favorites, file, indent=4)


def add_favorite(city):
    favorites = load_favorites()
    if city not in favorites:
        favorites.append(city)
        save_favorites(favorites)
        print("⭐ City added to favorites.")
    else:
        print("ℹ City already in favorites.")


def view_favorites():
    favorites = load_favorites()
    if not favorites:
        print("📭 No favorite cities saved.")
        return

    print("\n⭐ Favorite Cities:")
    for city in favorites:
        print("-", city)


def menu():
    print("\n🌦 Weather App")
    print("1. Get Weather")
    print("2. View Favorite Cities")
    print("3. Exit")


def main():
    while True:
        menu()
        choice = input("Choose an option: ")

        if choice == '1':
            city = input("Enter city name: ")
            data = get_weather(city)

            if data:
                display_weather(data)
                save = input("Save this city to favorites? (y/n): ")
                if save.lower() == 'y':
                    add_favorite(city)

        elif choice == '2':
            view_favorites()

        elif choice == '3':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice.")


main()
