import os
import shutil

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}


def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"


def organize_folder(path):
    if not os.path.exists(path):
        print("❌ Folder does not exist.")
        return

    files = os.listdir(path)
    moved_count = {}

    for file in files:
        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            category = get_category(ext)

            category_folder = os.path.join(path, category)

            if not os.path.exists(category_folder):
                os.mkdir(category_folder)

            shutil.move(file_path, os.path.join(category_folder, file))
            moved_count[category] = moved_count.get(category, 0) + 1

    print("\n📁 File Organization Complete!")
    for category, count in moved_count.items():
        print(f"{category}: {count} files moved")


def main():
    print("🗂 File Organizer")
    target_folder = input("Enter folder path to organize: ")

    organize_folder(target_folder)


main()
