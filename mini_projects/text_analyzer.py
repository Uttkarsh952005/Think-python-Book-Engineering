"""
Mini Project: Text Analyzer
Project Integration Phase

Analyzes a given text and provides basic statistics: character count,
word count, and sentence count. Demonstrates string manipulation and
basic algorithms.
"""


def count_characters(text: str) -> int:
    """Returns the total number of characters (excluding spaces)."""
    return len(text.replace(" ", ""))


def count_words(text: str) -> int:
    """Returns the total number of words based on whitespace."""
    if not text.strip():
        return 0
    return len(text.split())


def count_sentences(text: str) -> int:
    """Returns an estimate of sentences by counting punctuation marks."""
    if not text.strip():
        return 0
    # Simple heuristic: count periods, exclamation marks, and question marks
    return sum(text.count(p) for p in ".!?")


def analyze_text(text: str) -> None:
    """Coordinates the analysis and prints the results."""
    print("\n--- Text Analysis Results ---")
    print(f"Characters (no spaces): {count_characters(text)}")
    print(f"Words:                  {count_words(text)}")
    print(f"Sentences:              {count_sentences(text)}")
    print("-----------------------------\n")


def main() -> None:
    print("Welcome to the Text Analyzer.")
    sample_text = input("Please enter some text to analyze:\n> ")
    analyze_text(sample_text)


if __name__ == "__main__":
    main()
