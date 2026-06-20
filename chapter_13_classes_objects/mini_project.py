"""
Chapter 13: Mini Project - 2D Collision Detector
Demonstrates combining multiple objects to compute spatial logic.
"""

class Point:
    pass

class Rectangle:
    pass

def create_rectangle(x: float, y: float, w: float, h: float) -> Rectangle:
    """Helper to quickly scaffold a rectangle."""
    r = Rectangle()
    r.width = w
    r.height = h
    r.corner = Point()
    r.corner.x = x
    r.corner.y = y
    return r

def is_point_inside(p: Point, r: Rectangle) -> bool:
    """Checks if a point falls within the bounds of a rectangle."""
    in_x = r.corner.x <= p.x <= r.corner.x + r.width
    in_y = r.corner.y <= p.y <= r.corner.y + r.height
    return in_x and in_y

def do_rectangles_overlap(r1: Rectangle, r2: Rectangle) -> bool:
    """
    Checks if two rectangles overlap using bounding box logic (AABB).
    Two rectangles overlap if their x and y projections overlap.
    """
    # Check X overlap
    overlap_x = (r1.corner.x < r2.corner.x + r2.width) and \
                (r1.corner.x + r1.width > r2.corner.x)
                
    # Check Y overlap
    overlap_y = (r1.corner.y < r2.corner.y + r2.height) and \
                (r1.corner.y + r1.height > r2.corner.y)
                
    return overlap_x and overlap_y

def main():
    print("--- 2D Collision Detector ---")
    # Screen bounding box
    screen = create_rectangle(0, 0, 800, 600)
    
    # Player character box
    player = create_rectangle(400, 300, 50, 50)
    
    # Enemy box
    enemy = create_rectangle(420, 320, 50, 50)
    
    # Click point
    click = Point()
    click.x, click.y = 410, 310
    
    print(f"Is click inside player? {is_point_inside(click, player)}")
    print(f"Does player overlap enemy? {do_rectangles_overlap(player, enemy)}")
    print(f"Does enemy overlap screen? {do_rectangles_overlap(enemy, screen)}")

if __name__ == "__main__":
    main()
