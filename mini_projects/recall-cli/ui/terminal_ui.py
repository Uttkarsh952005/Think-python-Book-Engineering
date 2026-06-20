"""
Presentation Layer for RecallCLI.
Handles all rich terminal rendering. No domain logic lives here.
"""

from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text


class TerminalUI:
    """
    Handles all the terminal output using the rich library.
    """

    def __init__(self) -> None:
        self.console = Console()

    def display_welcome(self, title: str, card_count: int) -> None:
        """Renders the main welcome screen."""
        self.console.clear()

        # Build the content for the panel
        content = Text()
        content.append("A Command-Line Flashcard Learning Engine\n", style="dim italic")
        content.append(f"\nDeck: ", style="bold")
        content.append(f"{title}\n", style="cyan")
        content.append(f"Cards: ", style="bold")
        content.append(f"{card_count}", style="green")

        panel = Panel(
            content,
            title="[bold magenta]RecallCLI[/]",
            subtitle="[dim]Press Enter to begin[/]",
            expand=False,
            border_style="magenta",
            box=box.ROUNDED,
        )

        self.console.print()
        self.console.print(panel, justify="center")
        self.console.print()
        self.prompt_user("")  # Wait for Enter

    def display_error(self, message: str) -> None:
        """Renders an error panel cleanly."""
        panel = Panel(
            f"[bold red]{message}[/]",
            title="[bold red]Error[/]",
            expand=False,
            border_style="red",
        )
        self.console.print(panel)

    def display_question(
        self,
        question: str,
        question_num: int,
        total_questions: int,
        category: str,
        difficulty: str,
        payload: str = "",
    ) -> None:
        """Renders the flashcard question with category, difficulty, and optional payload."""
        self.console.print()

        # Color code the difficulty badge
        diff_color = "green"
        if difficulty.lower() == "medium":
            diff_color = "yellow"
        elif difficulty.lower() == "hard":
            diff_color = "red"

        header = f"[bold cyan]Question {question_num}/{total_questions}[/] | [dim]{category}[/] | [bold {diff_color}]{difficulty}[/]"

        content = Text.from_markup(f"[bold white]{question}[/]{payload}")

        panel = Panel(
            content, title=header, expand=False, border_style="cyan", box=box.ROUNDED
        )
        self.console.print(panel)

    def prompt_user(self, prompt_text: str = "Your answer: ") -> str:
        """Handles user input cleanly."""
        return self.console.input(f"[bold yellow]{prompt_text}[/] ").strip()

    def show_correct(self) -> None:
        """Feedback for correct answer."""
        self.console.print("[bold green]Correct![/]\n")

    def show_incorrect(self, correct_answer: str) -> None:
        """Feedback for completely incorrect answer (out of retries)."""
        self.console.print(
            f"[bold red]Incorrect.[/] The correct answer was: [bold green]{correct_answer}[/]\n"
        )

    def show_retry(self) -> None:
        """Feedback for an incorrect answer that can be retried."""
        self.console.print("[bold yellow]Incorrect. Try again![/]")

    def show_skipped(self, correct_answer: str) -> None:
        """Feedback when a question is skipped."""
        self.console.print(
            f"[dim]Skipped.[/] The correct answer was: [bold green]{correct_answer}[/]\n"
        )

    def display_summary(self, score: int, total: int, retries: int) -> None:
        """Renders the final quiz summary using a rich Table."""
        self.console.print()

        table = Table(title="[bold magenta]Session Summary[/]", box=box.SIMPLE_HEAVY)

        table.add_column("Metric", style="cyan", no_wrap=True)
        table.add_column("Result", style="bold green")

        accuracy = (score / total) * 100 if total > 0 else 0.0

        # Color coding the accuracy
        acc_str = f"{accuracy:.1f}%"
        if accuracy < 50:
            acc_str = f"[red]{acc_str}[/]"
        elif accuracy < 80:
            acc_str = f"[yellow]{acc_str}[/]"

        table.add_row("Questions Asked", str(total))
        table.add_row("Correct Answers", str(score))
        table.add_row("Accuracy", acc_str)
        table.add_row("Retries Used", str(retries))

        self.console.print(table)
        self.console.print()
