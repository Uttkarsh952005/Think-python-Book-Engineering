# Notes on Advanced Classes

- **The Power of `@property`**: In Java or C++, you are taught to make *everything* a getter/setter immediately `getName()`, `setName()`. In Python, you start with public attributes `obj.name`. If you later realize you need validation, you use `@property` to add the logic without breaking the API for everyone already using `obj.name`. It is incredibly elegant.
- **Factory Methods**: `__init__` is restrictive because you can only have one. `@classmethod` allows you to define as many clear, semantic entry points into your class as you need.
- **Single Underscore vs Double Underscore**: 
  - `_name`: "Please don't touch this, it's internal." (Convention).
  - `__name`: "I am aggressively mangling this name so subclasses don't accidentally overwrite it." (Enforced by interpreter). Usually overkill. Stick to single underscores.
