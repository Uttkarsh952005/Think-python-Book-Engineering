"""
Mini Project: Command Line Calculator
Project Integration Phase

A REPL (Read-Evaluate-Print Loop) calculator that safely parses
and evaluates basic arithmetic without relying on python's eval().
Demonstrates infinite loops, error handling, and string splitting.
"""


def perform_operation(num1: float, operator: str, num2: float) -> float:
    """Performs the mathematical operation based on the operator string."""
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError(f"Unknown operator: {operator}")


def parse_and_calculate(expression: str) -> float:
    """
    Parses a string like '5 + 3' into its components and calculates.
    Requires spaces between numbers and the operator.
    """
    parts = expression.split()
    if len(parts) != 3:
        raise ValueError(
            "Expression must be in format: number operator number (e.g. 5 + 3)"
        )

    num1 = float(parts[0])
    operator = parts[1]
    num2 = float(parts[2])

    return perform_operation(num1, operator, num2)


def main() -> None:
    print("--- Command Line Calculator ---")
    print("Type expressions like '5 + 3' or '10 / 2' (spaces required).")
    print("Type 'quit' or 'q' to exit.\n")

    while True:
        user_input = input("calc> ").strip()

        if user_input.lower() in ("quit", "q"):
            print("Exiting calculator. Goodbye!")
            break

        if not user_input:
            continue

        try:
            result = parse_and_calculate(user_input)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Input Error: {e}")
        except ZeroDivisionError as e:
            print(f"Math Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
