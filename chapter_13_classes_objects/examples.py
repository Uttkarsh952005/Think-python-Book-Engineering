"""
Chapter 13: Classes and Objects
Examples of defining classes, instantiating objects, and managing state.
"""
import copy

class Point:
    """Represents a point in 2D space."""
    # In this early chapter, we define empty classes and add attributes later.
    # Note: Modern Python usually initializes attributes in an __init__ method.
    pass

class Rectangle:
    """Represents a rectangle. Attributes: width, height, corner."""
    pass

def demonstrate_aliasing_and_copying() -> None:
    """Shows how the copy module prevents aliasing bugs."""
    p1 = Point()
    p1.x = 3.0
    p1.y = 4.0
    
    # Alias: both variables point to the same object in memory
    p2 = p1
    
    # Shallow Copy: creates a new object
    p3 = copy.copy(p1)
    
    # Modifying p1 affects p2, but not p3
    p1.x = 99.0
    
    print(f"p1: ({p1.x}, {p1.y})")
    print(f"p2 (Alias): ({p2.x}, {p2.y})  <- Changed with p1")
    print(f"p3 (Copy): ({p3.x}, {p3.y})  <- Remained independent")

def main():
    print("--- Instantiating Objects ---")
    blank = Point()
    blank.x = 3.0
    blank.y = 4.0
    print(f"Point created at ({blank.x}, {blank.y})")
    
    print("\n--- Complex Objects ---")
    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0
    print(f"Rectangle {box.width}x{box.height} at ({box.corner.x}, {box.corner.y})")
    
    print("\n--- Aliasing vs Copying ---")
    demonstrate_aliasing_and_copying()

if __name__ == "__main__":
    main()
