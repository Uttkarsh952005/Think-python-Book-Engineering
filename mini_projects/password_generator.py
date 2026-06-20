"""
Mini Project: Password Generator
Project Integration Phase

Generates strong, secure, and customizable random passwords.
Demonstrates the `random` and `string` modules, loops, and list joining.
"""

import random
import string


def generate_password(
    length: int = 12,
    use_uppercase: bool = True,
    use_numbers: bool = True,
    use_symbols: bool = True,
) -> str:
    """
    Generates a random password based on the specified constraints.
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters.")

    # Start with base lowercase letters
    character_pool = list(string.ascii_lowercase)
    guaranteed_chars = [random.choice(string.ascii_lowercase)]

    if use_uppercase:
        character_pool.extend(string.ascii_uppercase)
        guaranteed_chars.append(random.choice(string.ascii_uppercase))

    if use_numbers:
        character_pool.extend(string.digits)
        guaranteed_chars.append(random.choice(string.digits))

    if use_symbols:
        # Using a safe subset of symbols
        symbols = "!@#$%^&*"
        character_pool.extend(symbols)
        guaranteed_chars.append(random.choice(symbols))

    # Fill the rest of the password length from the combined pool
    remaining_length = length - len(guaranteed_chars)
    password_chars = guaranteed_chars + random.choices(
        character_pool, k=remaining_length
    )

    # Shuffle to ensure the guaranteed characters aren't always at the start
    random.shuffle(password_chars)

    return "".join(password_chars)


def main() -> None:
    print("--- Secure Password Generator ---")
    try:
        length = int(input("Enter password length (e.g., 16): "))
        password = generate_password(
            length=length, use_uppercase=True, use_numbers=True, use_symbols=True
        )
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
