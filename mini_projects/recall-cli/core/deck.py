"""
Deck Model for RecallCLI.
Represents a collection of Flashcards (Composition).
"""

from typing import List, Optional

from core.flashcard import Flashcard


class Deck:
    """
    Manages a collection of Flashcard objects.
    Demonstrates the HAS-A relationship (Composition).
    """

    def __init__(self, title: str) -> None:
        self.title = title
        self.cards: List[Flashcard] = []

    def __str__(self) -> str:
        return f"Deck: '{self.title}' ({len(self.cards)} cards)"

    def add_card(self, card: Flashcard) -> None:
        """Adds a new Flashcard object to the deck."""
        self.cards.append(card)

    def get_card(self, index: int) -> Optional[Flashcard]:
        """Safely retrieves a card by index. Returns None if out of bounds."""
        if 0 <= index < len(self.cards):
            return self.cards[index]
        return None

    def display_all(self) -> None:
        """A simple procedural method to dump all cards to the console."""
        print(f"--- {self.title} ---")
        for idx, card in enumerate(self.cards):
            print(f"[{idx}] {card}")
