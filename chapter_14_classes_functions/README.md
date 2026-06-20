# Chapter 14: Classes and Functions

This chapter explores how functions interact with programmer-defined types, specifically introducing the distinction between pure functions and modifiers.

## Core Concepts
- **Pure Functions**: A function that takes objects as arguments, does not modify any of them, and returns a new value or object.
- **Modifiers**: A function that changes the state of one or more of the objects it receives as arguments.
- **Prototyping vs Planning**: 
  - *Prototyping*: Writing code quickly to see if it works, then finding edge cases (like time wrapping over 60 seconds) and patching them.
  - *Planned Development*: Thinking about the problem domain (e.g., converting Time to an integer of total seconds, doing the math, and converting back).

## Engineering Takeaways
- **Prefer Pure Functions**: Whenever possible, write pure functions. They are easier to test, easier to reason about, and eliminate an entire class of aliasing bugs.
- **When to use Modifiers**: Modifiers are useful when copying large objects is prohibitively expensive in terms of memory or performance.
- **Data Representation**: How you represent data internally matters. Representing time as hours, minutes, and seconds is intuitive for humans but difficult for math. Representing it internally as `total_seconds` makes the math trivial.
