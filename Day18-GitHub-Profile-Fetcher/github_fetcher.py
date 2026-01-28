import requests
import json
import os

PROFILE_FILE = "profiles.json"
BASE_URL = "https://api.github.com/users"


def fetch_user(username):
    response = requests.get(f"{BASE_URL}/{username}")
    if response.status_code != 200:
        print("❌ User not found.")
        return None
    return response.json()


def fetch_repos(username):
    response = requests.get(f"{BASE_URL}/{username}/repos")
    if response.status_code != 200:
        return []
    return response.json()


def load_profiles():
    if not os.path.exists(PROFILE_FILE):
        return {}

    with open(PROFILE_FILE, "r") as file:
        return json.load(file)


def save_profiles(data):
    with open(PROFILE_FILE, "w") as file:
        json.dump(data, file, indent=4)


def show_profile(user, repos):
    print("\n🐙 GitHub Profile")
    print(f"Username: {user['login']}")
    print(f"Public Repos: {user['public_repos']}")
    print(f"Followers: {user['followers']}")
    print(f"Following: {user['following']}")

    print("\n⭐ Top Repositories:")
    sorted_repos = sorted(repos, key=lambda r: r["stargazers_count"], reverse=True)

    for repo in sorted_repos[:5]:
        print(f"- {repo['name']} ⭐ {repo['stargazers_count']}")


def language_stats(repos):
    languages = {}

    for repo in repos:
        lang = repo["language"]
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    return languages


def main():
    username = input("Enter GitHub username: ").strip()

    user = fetch_user(username)
    if not user:
        return

    repos = fetch_repos(username)

    show_profile(user, repos)

    langs = language_stats(repos)
    print("\n📊 Language Breakdown:")
    for lang, count in langs.items():
        print(f"{lang}: {count}")

    save = input("\nSave profile data? (y/n): ")
    if save.lower() == 'y':
        profiles = load_profiles()
        profiles[username] = {
            "followers": user["followers"],
            "repos": user["public_repos"],
            "languages": langs
        }
        save_profiles(profiles)
        print("💾 Profile saved.")


main()
