import json
import time
import os


def load_questions():
    """
    Loads questions.json from the same directory as quiz.py
    This avoids file not found errors.
    """
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "questions.json")

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def run_quiz(questions):
    score = 0
    wrong_questions = []

    start_time = time.time()

    for i, question in enumerate(questions, start=1):
        print(f"\nQ{i}: {question['question']}")

        for idx, option in enumerate(question["options"], start=1):
            print(f"{idx}. {option}")

        user_input = input("Your answer (number): ").strip()

        if user_input.isdigit():
            selected_index = int(user_input) - 1

            if 0 <= selected_index < len(question["options"]):
                selected_answer = question["options"][selected_index]

                if selected_answer == question["answer"]:
                    print("✅ Correct!")
                    score += 1
                else:
                    print(f"❌ Wrong. Correct answer: {question['answer']}")
                    wrong_questions.append(question)
            else:
                print(f"❌ Invalid option. Correct answer: {question['answer']}")
                wrong_questions.append(question)
        else:
            print(f"❌ Invalid input. Correct answer: {question['answer']}")
            wrong_questions.append(question)

    end_time = time.time()
    total_time = end_time - start_time

    return score, total_time, wrong_questions


def show_summary(score, total_questions, time_taken, wrong_questions):
    print("\n🏁 QUIZ FINISHED")
    print("-" * 30)
    print(f"Score: {score} / {total_questions}")
    print(f"Time Taken: {time_taken:.2f} seconds")

    if wrong_questions:
        print("\n📌 Review Incorrect Questions:")
        for q in wrong_questions:
            print(f"- {q['question']} (Answer: {q['answer']})")
    else:
        print("\n🎉 Perfect score! Well done!")


def main():
    print("🧠 Welcome to the Quiz Game")

    try:
        questions = load_questions()
    except FileNotFoundError:
        print("❌ questions.json file not found.")
        return
    except json.JSONDecodeError:
        print("❌ Error reading questions.json (invalid JSON).")
        return

    score, time_taken, wrong_questions = run_quiz(questions)
    show_summary(score, len(questions), time_taken, wrong_questions)


main()

