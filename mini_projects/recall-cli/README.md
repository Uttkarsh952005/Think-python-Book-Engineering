# RecallCLI

A terminal-based flashcard engine I built as the final capstone project for my *Think Python* study journey. 

The goal wasn't just to build a working flashcard app, but to practice applying Python software engineering concepts—like separating the UI from the underlying logic, and using inheritance to handle different types of cards cleanly.

## Features
- **Clean Architecture**: The terminal UI is completely decoupled from the core quiz logic.
- **Multiple Card Types**: Supports basic Q&A, Multiple Choice, and True/False cards using simple OOP polymorphism.
- **JSON Storage**: Saves and loads decks via explicit JSON serialization rather than relying on `pickle`.
- **Session Tracking**: Tracks basic correct/incorrect attempts during a study session.

## Architecture

I organized the project to keep different responsibilities isolated:

- `core/`: The Python domain models (`Flashcard`, `Deck`, `QuizEngine`). No UI or storage code lives here.
- `storage/`: Handles reading/writing the `sample_deck.json`. 
- `ui/`: Manages the terminal output using `rich`. The engine just calls `ui.display_question()`.
- `data/`: Where the JSON decks actually live.

### OOP Concepts Practiced
- **Composition**: A `Deck` manages a list of `Flashcard` instances.
- **Inheritance & Polymorphism**: `MultipleChoiceCard` and `TrueFalseCard` inherit from `Flashcard`. The `QuizEngine` just calls `card.check_answer()` without needing messy `if/elif` type checks.

## Example Deck Format

The persistence layer maps objects to plain JSON. 

```json
{
    "type": "multiple_choice",
    "question": "What is the 'Diamond Problem'?",
    "answer": "Multiple Inheritance Ambiguity",
    "options": ["Memory Leak", "Multiple Inheritance Ambiguity", "Infinite Recursion", "Database Deadlock"],
    "category": "OOP",
    "difficulty": "Hard"
}
```

## Running the Project

```bash
pip install -r requirements.txt
python main.py
```

## Future Improvements
- **Spaced Repetition**: Right now the engine just picks a random sample. It would be cool to add a basic algorithm based on previous `times_correct`.
- **Error Handling**: The JSON loader is a bit brittle if the file is manually edited incorrectly.
- **YAML Support**: JSON is fine, but YAML would be much easier to hand-write decks for.

*See `ENGINEERING_NOTES.md` and `LEARNING_NOTES.md` for my thoughts on the design choices and mistakes made during development.*
