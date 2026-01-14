import string

def analyze_text(text):
    # Remove punctuation for accurate word counting
    cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

    words = cleaned_text.lower().split()
    word_count = len(words)

    char_count = len(text)
    sentence_count = text.count('.') + text.count('!') + text.count('?')
    paragraph_count = text.count('\n\n') + 1

    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return word_count, char_count, sentence_count, paragraph_count, frequency


def display_top_words(freq, top_n=5):
    sorted_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    print("\n Most Frequent Words:")
    for word, count in sorted_words[:top_n]:
        print(f"{word}: {count}")


def save_report(data):
    with open("report.txt", "w") as file:
        file.write("TEXT ANALYSIS REPORT\n\n")
        file.write(f"Words: {data[0]}\n")
        file.write(f"Characters: {data[1]}\n")
        file.write(f"Sentences: {data[2]}\n")
        file.write(f"Paragraphs: {data[3]}\n\n")

    print("Report saved as report.txt")


def main():
    print("Word Counter")

    choice = input("Analyze (1) Text input or (2) File? ")

    if choice == '1':
        text = input("\nEnter text:\n")
    elif choice == '2':
        filename = input("Enter filename: ")
        try:
            with open(filename, "r") as file:
                text = file.read()
        except FileNotFoundError:
            print("File not found.")
            return
    else:
        print("Invalid choice.")
        return

    data = analyze_text(text)

    print("\n--- Analysis Result ---")
    print(f"Words: {data[0]}")
    print(f"Characters: {data[1]}")
    print(f"Sentences: {data[2]}")
    print(f"Paragraphs: {data[3]}")

    display_top_words(data[4])

    save = input("\nSave report? (y/n): ")
    if save.lower() == 'y':
        save_report(data)


main()
