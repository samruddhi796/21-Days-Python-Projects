import random

choices = ["rock", "paper", "scissors"]

ascii_art = {
    "rock": "✊",
    "paper": "✋",
    "scissors": "✌"
}

def get_winner(player, computer):
    if player == computer:
        return "draw"
    elif (
        (player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper")
    ):
        return "player"
    else:
        return "computer"


print("🎮 Rock Paper Scissors")

while True:
    rounds = input("Choose match type (3 / 5 / 7): ")
    if rounds in ["3", "5", "7"]:
        rounds = int(rounds)
        break
    else:
        print("❌ Invalid choice.")

player_score = 0
computer_score = 0
player_choices = []

while player_score < rounds and computer_score < rounds:
    player = input("\nChoose rock, paper, or scissors: ").lower()

    if player not in choices:
        print("❌ Invalid move.")
        continue

    computer = random.choice(choices)
    player_choices.append(player)

    print(f"You chose {ascii_art[player]}  | Computer chose {ascii_art[computer]}")

    winner = get_winner(player, computer)

    if winner == "player":
        player_score += 1
        print("✅ You win this round!")
    elif winner == "computer":
        computer_score += 1
        print("❌ Computer wins this round!")
    else:
        print("⚖ It's a draw!")

    print(f"Score → You: {player_score} | Computer: {computer_score}")

print("\n🏁 Match Over!")

if player_score > computer_score:
    print("🎉 You won the match!")
else:
    print("😢 Computer won the match.")

total_games = player_score + computer_score
win_rate = (player_score / total_games) * 100 if total_games > 0 else 0

most_picked = max(set(player_choices), key=player_choices.count)

print("\n📊 Game Statistics")
print(f"Total Rounds Played: {total_games}")
print(f"Your Win Rate: {win_rate:.2f}%")
print(f"Most Picked Choice: {most_picked}")
