# Notes on Classes and Objects

- **Delayed Initialization**: In this chapter, we create an empty class `pass` and attach attributes to the instance later (`box.width = 100`). While educational for understanding memory, this is generally considered **bad practice** in modern Python engineering. Attributes should be defined inside an `__init__` method so the object is fully formed upon creation. We will evolve to this in later chapters.
- **Shallow vs Deep Copy**: `copy.copy()` copies the object and the *references* to its attributes. If an object contains another object (like a Rectangle containing a Point), a shallow copy shares the inner Point. `copy.deepcopy()` recursively copies everything, creating a completely independent structure.
- **`isinstance()` and `hasattr()`**: Built-in functions to safely check an object's type or properties before interacting with it.
