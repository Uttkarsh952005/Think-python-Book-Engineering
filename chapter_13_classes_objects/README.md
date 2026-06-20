# Chapter 13: Classes and Objects

Until now, we've used Python's built-in types (strings, lists, dictionaries). This chapter introduces the ability to create our own **programmer-defined types** using classes.

## Core Concepts
- **Class**: A blueprint or template for a user-defined type.
- **Instance**: A specific object created from a class.
- **Instantiation**: The process of creating a new object.
- **Attributes**: Named values associated with an object (e.g., `p.x` and `p.y`).
- **State**: The values of an object's attributes at a given time.

## Engineering Takeaways
- **Classes vs Instances**: A class is like the concept of a "Car". An instance is your specific Honda Civic parked outside.
- **Objects are Mutable**: By default, you can change the state of an object by reassigning its attributes. This is powerful but requires careful tracking of aliasing.
- **Copying**: Because objects are mutable, aliasing (`p1 = p2`) can lead to bugs. Use the `copy` module (`copy.copy()` or `copy.deepcopy()`) to create independent clones of objects.
