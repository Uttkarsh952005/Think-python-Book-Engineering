# Notes on Advanced Inheritance

- **Composition > Inheritance**: Even advanced inheritance should be used sparingly. A `LoggerMixin` is neat, but passing a `logger` object to the `DatabaseNode` constructor (Dependency Injection) is often much easier to test and maintain.
- **ABC enforces structure**: Abstract Base Classes are the Python equivalent of Interfaces in Java. They are essential for building plugins or forcing junior developers to comply with an architectural pattern before the code even runs.
- **Multiple Inheritance Warning**: Multiple inheritance is heavily discouraged in many modern languages (Java and C# forbid it entirely for classes). Python allows it, but deep multiple inheritance hierarchies become an unreadable nightmare of MRO traces. Use simple Mixins, or don't use it at all.
