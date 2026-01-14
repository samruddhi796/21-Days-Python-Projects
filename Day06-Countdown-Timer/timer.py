import time

def convert_to_seconds(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


def format_time(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


print("Countdown Timer")

try:
    h = int(input("Enter hours: "))
    m = int(input("Enter minutes: "))
    s = int(input("Enter seconds: "))
except ValueError:
    print("Please enter valid numbers.")
    exit()

total_seconds = convert_to_seconds(h, m, s)

paused = False

while total_seconds > 0:
    if not paused:
        print("\rTime Left:", format_time(total_seconds), end="")
        time.sleep(1)
        total_seconds -= 1

    if total_seconds % 5 == 0:
        command = input("\nPress 'p' to pause, 'r' to resume, Enter to continue: ")
        if command.lower() == 'p':
            paused = True
        elif command.lower() == 'r':
            paused = False

print("\n Time's up!\a")
