import re
import os


def get_common_passwords_path():
    """
    Returns the absolute path of common_passwords.txt
    relative to this script.
    """
    base_dir = os.path.dirname(__file__)
    return os.path.join(base_dir, "common_passwords.txt")


def check_common(password):
    file_path = get_common_passwords_path()

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            common = file.read().splitlines()
        return password.lower() in common
    except FileNotFoundError:
        print("⚠ common_passwords.txt not found. Skipping common password check.")
        return False


def check_strength(password):
    score = 0
    feedback = []

    # Length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    # Uppercase
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    # Lowercase
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    # Numbers
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    # Symbols
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    return score, feedback


def estimate_crack_time(score):
    if score <= 2:
        return "Instantly"
    elif score == 3:
        return "Minutes"
    elif score == 4:
        return "Hours"
    else:
        return "Years"


def main():
    print("🔐 Password Strength Checker")

    password = input("Enter password: ").strip()

    if not password:
        print("❌ Password cannot be empty.")
        return

    if check_common(password):
        print("❌ This password is too common.")
        print("Strength: Very Weak")
        print("Estimated time to crack: Instantly")
        return

    score, feedback = check_strength(password)

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    print("\n📊 Password Analysis")
    print(f"Strength: {strength}")
    print(f"Estimated time to crack: {estimate_crack_time(score)}")

    if feedback:
        print("\nSuggestions to improve:")
        for item in feedback:
            print("-", item)
    else:
        print("✅ Excellent password!")


main()

