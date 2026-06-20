"""
Mini Project: Typing Speed Tester
Project Integration Phase

Measures typing speed in Words Per Minute (WPM).
Demonstrates working with the time module, user input, and string comparison.
"""

import time


def calculate_wpm(start_time: float, end_time: float, typed_text: str) -> float:
    """
    Calculates words per minute.
    Standard metric: 1 word = 5 characters.
    """
    time_elapsed_minutes = (end_time - start_time) / 60.0
    num_characters = len(typed_text)
    num_words = num_characters / 5.0

    if time_elapsed_minutes == 0:
        return 0.0
    return num_words / time_elapsed_minutes


def calculate_accuracy(prompt: str, typed: str) -> float:
    """Calculates accuracy percentage based on matching characters."""
    if not prompt:
        return 0.0
    correct_chars = sum(1 for p, t in zip(prompt, typed) if p == t)
    # Penalize for missing or extra characters
    length_penalty = abs(len(prompt) - len(typed))
    correct_chars = max(0, correct_chars - length_penalty)
    return (correct_chars / len(prompt)) * 100.0


def run_test(prompt_text: str) -> None:
    """Runs a single typing test session."""
    print("Type the following text as quickly and accurately as possible:\n")
    print(f"--> '{prompt_text}'\n")
    input("Press ENTER when you are ready to start...")

    print("\nGO!")
    start_time = time.time()
    typed_text = input("> ")
    end_time = time.time()

    wpm = calculate_wpm(start_time, end_time, typed_text)
    accuracy = calculate_accuracy(prompt_text, typed_text)
    time_taken = end_time - start_time

    print("\n--- Results ---")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Speed:      {wpm:.2f} WPM")
    print(f"Accuracy:   {accuracy:.2f}%")


def main() -> None:
    test_phrase = "The quick brown fox jumps over the lazy dog."
    print("Welcome to the Typing Speed Tester.")
    run_test(test_phrase)


if __name__ == "__main__":
    main()
