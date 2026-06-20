"""
Chapter 14: Exercises
Implementing modifiers and pure functions using designed development.
"""

class Time:
    """Represents the time of day."""
    pass

# --- Designed Development Helpers ---

def time_to_int(t: Time) -> int:
    """Computes the number of seconds since midnight."""
    minutes = t.hour * 60 + t.minute
    seconds = minutes * 60 + t.second
    return seconds

def int_to_time(seconds: int) -> Time:
    """Makes a new Time object from seconds since midnight."""
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t

# --- Pure Functions vs Modifiers ---

def add_time(t1: Time, t2: Time) -> Time:
    """
    Pure Function: Adds two times using base-60 integer conversion.
    Returns a new Time object.
    """
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

def increment(t: Time, seconds: int) -> None:
    """
    Modifier: Adds seconds to a Time object in-place.
    """
    total_seconds = time_to_int(t) + seconds
    
    # Update the object in place
    new_t = int_to_time(total_seconds)
    t.hour = new_t.hour
    t.minute = new_t.minute
    t.second = new_t.second

def print_time(t: Time) -> None:
    print(f"{t.hour:02d}:{t.minute:02d}:{t.second:02d}")

if __name__ == "__main__":
    t1 = Time()
    t1.hour, t1.minute, t1.second = 9, 45, 0
    
    print("--- Pure Function (add_time) ---")
    duration = Time()
    duration.hour, duration.minute, duration.second = 1, 35, 0
    
    done = add_time(t1, duration)
    print("Start:    ", end=""); print_time(t1)
    print("Duration: ", end=""); print_time(duration)
    print("End:      ", end=""); print_time(done)
    
    print("\n--- Modifier (increment) ---")
    print("Before increment: ", end=""); print_time(t1)
    increment(t1, 3600) # Add 1 hour
    print("After increment:  ", end=""); print_time(t1)
