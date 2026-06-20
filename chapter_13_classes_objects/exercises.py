"""
Chapter 13: Exercises
Functions that take objects as parameters and return objects as results.
"""
import math
import copy

class Point:
    """Represents a point in 2-D space."""
    pass

class Rectangle:
    """Represents a rectangle. Attributes: width, height, corner."""
    pass

def distance_between_points(p1: Point, p2: Point) -> float:
    """Computes the Euclidean distance between two Point objects."""
    dx = p2.x - p1.x
    dy = p2.y - p1.y
    return math.sqrt(dx**2 + dy**2)

def move_rectangle(rect: Rectangle, dx: float, dy: float) -> None:
    """
    Modifies the Rectangle object by adding dx to the x coordinate
    of the corner and dy to the y coordinate of the corner.
    """
    rect.corner.x += dx
    rect.corner.y += dy

def move_rectangle_copy(rect: Rectangle, dx: float, dy: float) -> Rectangle:
    """
    Pure function: Creates and returns a new Rectangle instead of modifying the old one.
    """
    # Requires a deepcopy because Rectangle contains a Point
    new_rect = copy.deepcopy(rect)
    move_rectangle(new_rect, dx, dy)
    return new_rect

if __name__ == "__main__":
    print("--- Distance Between Points ---")
    p1 = Point()
    p1.x, p1.y = 0, 0
    p2 = Point()
    p2.x, p2.y = 3, 4
    print(f"Distance: {distance_between_points(p1, p2)}")
    
    print("\n--- Move Rectangle (Modifier vs Pure Function) ---")
    box = Rectangle()
    box.width, box.height = 50, 100
    box.corner = Point()
    box.corner.x, box.corner.y = 0, 0
    
    print(f"Original Corner: ({box.corner.x}, {box.corner.y})")
    
    # Pure function usage
    box2 = move_rectangle_copy(box, 10, 20)
    print(f"Pure Return Corner: ({box2.corner.x}, {box2.corner.y})")
    print(f"Original Corner (unchanged): ({box.corner.x}, {box.corner.y})")
    
    # Modifier usage
    move_rectangle(box, 5, 5)
    print(f"Modifier Corner (mutated): ({box.corner.x}, {box.corner.y})")
