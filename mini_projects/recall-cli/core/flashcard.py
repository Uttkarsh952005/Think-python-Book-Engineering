"""
Flashcard Models for RecallCLI.
Demonstrates Inheritance and Polymorphism.
"""

from typing import List, Optional, Tuple


class Flashcard:
    """
    Base class for flashcards. Subclasses should override get_payload() and check_answer().
    """

    def __init__(
        self,
        question: str,
        answer: str,
        category: str = "General",
        difficulty: str = "Medium",
    ) -> None:
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

        self.times_reviewed: int = 0
        self.times_correct: int = 0

    def check_answer(self, user_answer: str) -> bool:
        """Default validation logic. Can be overridden by subclasses."""
        self.times_reviewed += 1
        is_correct = user_answer.strip().lower() == str(self.answer).strip().lower()
        if is_correct:
            self.times_correct += 1
        return is_correct

    def get_payload(self) -> str:
        """
        Polymorphic method. Returns any extra information needed to display the question.
        For a base card, there is no extra payload.
        """
        return ""


class BasicFlashcard(Flashcard):
    """A standard text-based question and answer."""

    pass


class MultipleChoiceCard(Flashcard):
    """
    A multiple-choice flashcard.
    Stores a list of options and overrides payload generation and validation.
    """

    def __init__(
        self,
        question: str,
        answer: str,
        options: List[str],
        category: str = "General",
        difficulty: str = "Medium",
    ) -> None:
        # Call the parent constructor using super()
        super().__init__(question, answer, category, difficulty)
        self.options = options

    def get_payload(self) -> str:
        """Overrides the base method to return the multiple-choice options."""
        payload = "\n"
        # Create standard A, B, C, D formatting
        labels = ["A", "B", "C", "D", "E"]
        for i, option in enumerate(self.options):
            label = labels[i] if i < len(labels) else str(i)
            payload += f"  [bold cyan]{label}.[/] {option}\n"
        return payload

    def check_answer(self, user_answer: str) -> bool:
        """
        Overrides validation to accept the letter OR the full text.
        """
        self.times_reviewed += 1
        user_clean = user_answer.strip().lower()
        ans_clean = str(self.answer).strip().lower()

        # Determine which letter the correct answer corresponds to
        correct_letter = ""
        labels = ["a", "b", "c", "d", "e"]
        for i, option in enumerate(self.options):
            if str(option).strip().lower() == ans_clean:
                correct_letter = labels[i]
                break

        is_correct = (user_clean == ans_clean) or (user_clean == correct_letter)
        if is_correct:
            self.times_correct += 1
        return is_correct


class TrueFalseCard(Flashcard):
    """
    A True/False flashcard.
    Overrides validation to accept flexible inputs.
    """

    def __init__(
        self,
        question: str,
        answer: bool,
        category: str = "General",
        difficulty: str = "Medium",
    ) -> None:
        # The answer must be a boolean, but we store it as a string representation
        # for consistency with the base class architecture.
        super().__init__(question, str(answer), category, difficulty)

    def get_payload(self) -> str:
        return "\n  [bold cyan]True[/] or [bold cyan]False[/]?"

    def check_answer(self, user_answer: str) -> bool:
        """Flexible validation for T/F."""
        self.times_reviewed += 1

        user_clean = user_answer.strip().lower()
        correct_bool = self.answer.lower() == "true"

        # Map acceptable user inputs to booleans
        user_is_true = user_clean in ["true", "t", "yes", "y"]
        user_is_false = user_clean in ["false", "f", "no", "n"]

        # If they didn't type a recognizable boolean, fail them
        if not user_is_true and not user_is_false:
            return False

        is_correct = user_is_true == correct_bool
        if is_correct:
            self.times_correct += 1

        return is_correct
