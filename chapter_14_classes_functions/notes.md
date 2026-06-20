# Notes on Classes and Functions

- **The Prototype and Patch approach**: It's tempting to write an `add_time` function by simply adding seconds, then realizing you need an `if seconds >= 60`, then doing the same for minutes. This leads to bloated, error-prone code.
- **Designed Development**: The elegant solution is to convert the `Time` object to a single integer (`time_to_int`), perform standard addition, and convert it back (`int_to_time`). This demonstrates how changing your internal data representation drastically simplifies algorithms.
- **Invariants**: Conditions that should always be true (e.g., `0 <= minute < 60`). Assertions (`assert time.minute < 60`) are powerful tools for catching bugs early when writing modifiers.
