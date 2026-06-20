"""
Mini Project: Simple Quiz Engine
Project Integration Phase

A basic quiz engine that tests the user's knowledge.
Demonstrates dictionaries, iteration, and basic scoring logic.
"""

from typing import Dict


def run_quiz(questions: Dict[str, str]) -> None:
    """
    Iterates through a dictionary of questions and answers,
    prompting the user and tracking their score.
    """
    score = 0
    total = len(questions)

    print("\n--- Starting Quiz ---")
    print("Type your answer and press ENTER.\n")

    for question, correct_answer in questions.items():
        print(f"Q: {question}")
        user_answer = input("A: ").strip()

        # Simple case-insensitive comparison
        if user_answer.lower() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was: {correct_answer}\n")

    # Calculate percentage
    percentage = (score / total) * 100
    print("--- Quiz Complete ---")
    print(f"You scored {score} out of {total} ({percentage:.1f}%)")


def main() -> None:
    # A dictionary mapping questions (keys) to answers (values)
    python_trivia = {
        "Who created Python?": "Guido van Rossum",
        "What data structure uses key-value pairs?": "Dictionary",
        "What keyword is used to define a function?": "def",
        "Are Python lists mutable or immutable?": "mutable",
    }

    print("Welcome to the Python Trivia Quiz!")
    run_quiz(python_trivia)


if __name__ == "__main__":
    main()
