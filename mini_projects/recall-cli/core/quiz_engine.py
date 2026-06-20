"""
Quiz Engine for RecallCLI.
Orchestrates the learning session logic, tracking scores and serving cards.
"""

import random
from typing import Any, Optional

from core.deck import Deck
from core.flashcard import Flashcard


class QuizEngine:
    """
    Manages the flow of a study session.
    Takes a Deck and a UI object so it doesn't have to handle printing directly.
    """

    def __init__(self, deck: Deck, ui: Any) -> None:
        self.deck = deck
        self.ui = ui
        self.score: int = 0
        self.questions_asked: int = 0
        self.total_retries: int = 0

    def run_quiz(self, num_questions: int = 5) -> None:
        """Executes a quiz session for a specified number of questions."""
        if not self.deck.cards:
            self.ui.display_error(
                "The deck is empty. Add cards before starting a quiz."
            )
            return

        self.ui.display_welcome(self.deck.title, len(self.deck.cards))

        self.score = 0
        self.questions_asked = 0
        self.total_retries = 0

        total_to_ask = min(num_questions, len(self.deck.cards))
        session_cards = random.sample(self.deck.cards, total_to_ask)

        for card in session_cards:
            self._ask_card(card, total_to_ask)

        self.ui.display_summary(self.score, self.questions_asked, self.total_retries)

    def _ask_card(self, card: Flashcard, total_questions: int) -> None:
        """Handles the logic for a single card interaction, including retries."""
        self.questions_asked += 1

        # Polymorphic payload retrieval
        payload = card.get_payload()

        self.ui.display_question(
            card.question,
            self.questions_asked,
            total_questions,
            card.category,
            card.difficulty,
            payload,
        )

        attempts = 0
        max_attempts = 2

        while attempts < max_attempts:
            # We use the UI to get input
            user_answer = self.ui.prompt_user("Your answer (or 'skip'): ")

            if user_answer.lower() == "skip":
                self.ui.show_skipped(card.answer)
                break

            if card.check_answer(user_answer):
                self.ui.show_correct()
                self.score += 1
                break
            else:
                attempts += 1
                self.total_retries += 1
                if attempts < max_attempts:
                    self.ui.show_retry()
                else:
                    self.ui.show_incorrect(card.answer)
