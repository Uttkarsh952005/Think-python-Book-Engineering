"""
Chapter 17: Classes and Objects (Advanced)
Examples demonstrating properties, class methods, and encapsulation.
"""

class Temperature:
    """Represents a temperature, demonstrating managed attributes."""
    
    def __init__(self, celsius: float = 0.0):
        # We assign to the property, not the backing variable directly,
        # to ensure validation runs even during __init__.
        self.celsius = celsius

    @property
    def celsius(self) -> float:
        """The getter for celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value: float) -> None:
        """The setter for celsius, with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero is not possible.")
        self._celsius = value

    @property
    def fahrenheit(self) -> float:
        """A computed property. No setter is defined, so it's read-only."""
        return (self.celsius * 9 / 5) + 32

class User:
    """Demonstrates class methods as alternative constructors."""
    
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name: str) -> 'User':
        """Alternative constructor splitting a single string."""
        parts = full_name.split(' ', 1)
        first = parts[0]
        last = parts[1] if len(parts) > 1 else ""
        return cls(first, last)

def main():
    print("--- Properties and Validation ---")
    temp = Temperature(25)
    print(f"Celsius: {temp.celsius}")
    print(f"Fahrenheit: {temp.fahrenheit}")
    
    try:
        temp.celsius = -300 # Should trigger our validation
    except ValueError as e:
        print(f"Validation caught error: {e}")
        
    print("\n--- Alternative Constructors ---")
    user1 = User("Jane", "Doe")
    user2 = User.from_full_name("John Smith")
    print(f"User 1: {user1.first_name} {user1.last_name}")
    print(f"User 2: {user2.first_name} {user2.last_name}")

if __name__ == "__main__":
    main()
