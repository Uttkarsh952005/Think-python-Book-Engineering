"""
Chapter 14: Mini Project - Meeting Scheduler
Uses Time objects and pure functions to validate meeting schedules.
Demonstrates practical OOP modeling.
"""

class Time:
    pass

def make_time(h: int, m: int, s: int = 0) -> Time:
    """Factory function for cleaner initialization."""
    t = Time()
    t.hour, t.minute, t.second = h, m, s
    return t

def time_to_int(t: Time) -> int:
    return (t.hour * 60 + t.minute) * 60 + t.second

def is_overlap(start1: Time, end1: Time, start2: Time, end2: Time) -> bool:
    """
    Pure function. Checks if two time intervals overlap.
    Overlaps occur if Meeting 1 starts before Meeting 2 ends 
    AND Meeting 1 ends after Meeting 2 starts.
    """
    s1, e1 = time_to_int(start1), time_to_int(end1)
    s2, e2 = time_to_int(start2), time_to_int(end2)
    
    return s1 < e2 and e1 > s2

def main():
    print("--- Meeting Scheduler ---")
    
    # Meeting A: 10:00 to 11:30
    meet_a_start = make_time(10, 0)
    meet_a_end = make_time(11, 30)
    
    # Meeting B: 11:00 to 12:00 (Overlaps A)
    meet_b_start = make_time(11, 0)
    meet_b_end = make_time(12, 0)
    
    # Meeting C: 13:00 to 14:00 (No overlap)
    meet_c_start = make_time(13, 0)
    meet_c_end = make_time(14, 0)
    
    print(f"Does Meeting B overlap Meeting A? {is_overlap(meet_a_start, meet_a_end, meet_b_start, meet_b_end)}")
    print(f"Does Meeting C overlap Meeting A? {is_overlap(meet_a_start, meet_a_end, meet_c_start, meet_c_end)}")

if __name__ == "__main__":
    main()
