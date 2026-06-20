"""
Chapter 14: Classes and Functions
Examples using a Time class to demonstrate pure functions and modifiers.
"""

class Time:
    """
    Represents the time of day.
    Attributes: hour, minute, second.
    """
    pass

def print_time(t: Time) -> None:
    """Pure function to display time in HH:MM:SS format."""
    print(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}")

def is_after(t1: Time, t2: Time) -> bool:
    """
    Pure boolean function. Returns True if t1 follows t2 chronologically.
    """
    # A simple but slightly tedious comparison tree
    if t1.hour > t2.hour:
        return True
    if t1.hour < t2.hour:
        return False
        
    if t1.minute > t2.minute:
        return True
    if t1.minute < t2.minute:
        return False
        
    return t1.second > t2.second

def main():
    time1 = Time()
    time1.hour = 11
    time1.minute = 59
    time1.second = 30
    
    time2 = Time()
    time2.hour = 12
    time2.minute = 5
    time2.second = 0
    
    print("--- Time Objects ---")
    print_time(time1)
    print_time(time2)
    
    print("\n--- Pure Function Comparison ---")
    print(f"Is time1 after time2? {is_after(time1, time2)}")
    print(f"Is time2 after time1? {is_after(time2, time1)}")

if __name__ == "__main__":
    main()
