"""
Chapter 17: Exercises
Implementing a robust Fraction class with properties.
"""
import math

class Fraction:
    """Represents a mathematical fraction."""
    
    def __init__(self, numerator: int, denominator: int):
        self._numerator = numerator
        self.denominator = denominator # Uses the setter for validation
        self._simplify()

    @property
    def denominator(self) -> int:
        return self._denominator

    @denominator.setter
    def denominator(self, value: int) -> None:
        if value == 0:
            raise ValueError("Denominator cannot be zero.")
        self._denominator = value
        
    def _simplify(self) -> None:
        """Internal method to reduce the fraction."""
        gcd = math.gcd(self._numerator, self._denominator)
        self._numerator //= gcd
        self._denominator //= gcd
        
    def __str__(self) -> str:
        if self._denominator == 1:
            return str(self._numerator)
        return f"{self._numerator}/{self._denominator}"

if __name__ == "__main__":
    print("--- Fraction Initialization ---")
    f1 = Fraction(10, 20)
    print(f"10/20 simplified: {f1}")
    
    f2 = Fraction(5, 1)
    print(f"5/1 simplified: {f2}")
    
    print("\n--- Validation ---")
    try:
        f3 = Fraction(1, 0)
    except ValueError as e:
        print(f"Caught error: {e}")
