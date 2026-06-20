# Chapter 18: Inheritance (Advanced)

Inheritance goes beyond simply sharing methods. It provides a way to define strict structural contracts and compose behaviors from multiple sources.

## Core Concepts
- **Multiple Inheritance**: A class can inherit from more than one parent class. 
- **Method Resolution Order (MRO)**: The algorithm Python uses to decide which parent class's method to call when there are naming conflicts in multiple inheritance. (Accessible via `ClassName.__mro__`).
- **`super()` in depth**: `super()` doesn't just mean "parent". It means "the next class in the MRO". This is critical in multiple inheritance to ensure all initializers are called exactly once.
- **Abstract Base Classes (ABCs)**: Classes that cannot be instantiated on their own. They exist solely to define a strict interface (methods that *must* be overridden) for child classes.
- **Mixins**: Small classes that provide a specific piece of functionality. They are meant to be inherited alongside a primary base class, rather than instantiating on their own.

## Engineering Takeaways
- **The Diamond Problem**: When two parent classes inherit from the same grandparent, calling `super()` requires careful orchestration to avoid calling the grandparent's methods twice. Python handles this elegantly with C3 Linearization, but it requires developers to strictly use `super()` instead of hardcoding parent class names.
- **Contracts over Implementation**: Abstract Base Classes ensure that if an engineer creates a `Triangle` class inheriting from `Shape`, the system will literally refuse to run unless they implemented the `.area()` method. It enforces architectural discipline.
