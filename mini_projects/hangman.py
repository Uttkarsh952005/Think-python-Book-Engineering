"""
Mini Project: Hangman
Project Integration Phase

A classic word-guessing game.
Demonstrates working with sets, lists, strings, and while loops.
"""

import random


def get_word() -> str:
    """Returns a random word from a hardcoded list."""
    words = ["engineering", "python", "algorithm", "variable", "function", "compile"]
    return random.choice(words).upper()


def display_state(word: str, guessed_letters: set[str]) -> str:
    """
    Returns the current state of the word, revealing guessed letters
    and hiding unknown ones with underscores.
    """
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()


def play_hangman() -> None:
    word = get_word()
    guessed_letters: set[str] = set()
    attempts_remaining = 6

    print("--- Let's Play Hangman ---")

    while attempts_remaining > 0:
        current_display = display_state(word, guessed_letters)
        print(f"\nWord: {current_display}")
        print(f"Attempts left: {attempts_remaining}")

        # Check for win condition
        if "_" not in current_display:
            print("\nCongratulations! You guessed the word!")
            return

        guess = input("Guess a letter: ").upper().strip()

        # Input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            print(f"Incorrect! '{guess}' is not in the word.")
            attempts_remaining -= 1
        else:
            print(f"Good guess! '{guess}' is in the word.")

    print(f"\nGame Over! You ran out of attempts. The word was: {word}")


def main() -> None:
    play_hangman()


if __name__ == "__main__":
    main()
