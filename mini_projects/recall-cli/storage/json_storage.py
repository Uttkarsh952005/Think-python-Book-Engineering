"""
JSON Storage Layer for RecallCLI.
Handles reading and writing Decks to the filesystem.
"""

import json
import os
from typing import Optional

from core.deck import Deck
from core.flashcard import BasicFlashcard, Flashcard, MultipleChoiceCard, TrueFalseCard


class JSONStorage:
    """
    Handles reading and writing decks to JSON files.
    """

    @staticmethod
    def load_deck(filepath: str) -> Optional[Deck]:
        if not os.path.exists(filepath):
            print(f"Storage Error: File '{filepath}' not found.")
            return None

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)

            deck = Deck(data.get("title", "Untitled Deck"))

            raw_cards = data.get("cards", [])
            for rc in raw_cards:
                card_type = rc.get("type", "basic")
                question = rc.get("question", "")
                answer = rc.get("answer", "")
                category = rc.get("category", "General")
                difficulty = rc.get("difficulty", "Medium")

                if not question or answer == "":
                    continue

                # Explicit Type Mapping (Polymorphic instantiation)
                if card_type == "multiple_choice":
                    options = rc.get("options", [])
                    card = MultipleChoiceCard(
                        question, answer, options, category, difficulty
                    )
                elif card_type == "true_false":
                    card = TrueFalseCard(question, bool(answer), category, difficulty)
                    # Correct the stringified boolean if needed from storage
                    card.answer = str(answer)
                else:
                    card = BasicFlashcard(question, answer, category, difficulty)

                # Load stats
                card.times_reviewed = rc.get("times_reviewed", 0)
                card.times_correct = rc.get("times_correct", 0)

                deck.add_card(card)

            return deck

        except Exception as e:
            print(f"Storage Error: An unexpected error occurred: {e}")
            return None

    @staticmethod
    def save_deck(deck: Deck, filepath: str) -> bool:
        data = {"title": deck.title, "cards": []}

        for card in deck.cards:
            card_data = {
                "question": card.question,
                "answer": card.answer,
                "category": card.category,
                "difficulty": card.difficulty,
                "times_reviewed": card.times_reviewed,
                "times_correct": card.times_correct,
            }

            # Identify the specific subclass for serialization
            if isinstance(card, MultipleChoiceCard):
                card_data["type"] = "multiple_choice"
                card_data["options"] = card.options
            elif isinstance(card, TrueFalseCard):
                card_data["type"] = "true_false"
                # TrueFalseCard answer is technically stored as string ("True"/"False")
                card_data["answer"] = card.answer.lower() == "true"
            else:
                card_data["type"] = "basic"

            data["cards"].append(card_data)

        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4)
            return True
        except Exception as e:
            print(f"Storage Error: Could not save deck to '{filepath}': {e}")
            return False
