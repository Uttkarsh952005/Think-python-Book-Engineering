"""
Entry point for RecallCLI (Phase 3).
Demonstrates File I/O Persistence and the QuizEngine.
"""

import os

from core.quiz_engine import QuizEngine
from storage.json_storage import JSONStorage
from ui.terminal_ui import TerminalUI


def main() -> None:
    ui = TerminalUI()

    # Define our data path relative to this script
    base_dir = os.path.dirname(os.path.abspath(__file__))
    deck_path = os.path.join(base_dir, "data", "sample_deck.json")

    deck = JSONStorage.load_deck(deck_path)

    if deck is None:
        ui.display_error("Failed to load the deck from storage. Exiting.")
        return

    if not deck.cards:
        ui.display_error("The loaded deck contains no cards. Exiting.")
        return

    # Inject the UI dependency into the engine
    engine = QuizEngine(deck, ui)
    engine.run_quiz(num_questions=3)

    # Save progress back to storage so we don't lose review stats
    progress_path = os.path.join(base_dir, "data", "user_progress.json")
    JSONStorage.save_deck(deck, progress_path)


if __name__ == "__main__":
    main()
