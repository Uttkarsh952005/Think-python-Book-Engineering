"""
Chapter 18: Exercises
Implementing shape abstractions using ABCs.
"""
import math
from abc import ABC, abstractmethod

class Shape(ABC):
    """Strict contract for all geometric shapes."""
    
    @abstractmethod
    def area(self) -> float:
        pass
        
    @abstractmethod
    def perimeter(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
        
    def area(self) -> float:
        return math.pi * self.radius ** 2
        
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius

class Square(Shape):
    def __init__(self, side: float):
        self.side = side
        
    def area(self) -> float:
        return self.side ** 2
        
    def perimeter(self) -> float:
        return 4 * self.side

def print_shape_info(shape: Shape) -> None:
    """
    Because of the ABC contract, we know with 100% certainty 
    that area() and perimeter() exist.
    """
    print(f"Type: {shape.__class__.__name__}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print("-" * 20)

if __name__ == "__main__":
    print("--- Shape Contracts ---")
    c = Circle(5.0)
    s = Square(4.0)
    
    print_shape_info(c)
    print_shape_info(s)
