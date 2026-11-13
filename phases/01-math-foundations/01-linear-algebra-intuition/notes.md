# Lesson 1: Linear Algebra Intuition

## Segment 1 — Vector basics and magnitude

**Status:** Segment understood. The Python function was run successfully in my local environment and produced the three expected results.

### 1. What is a vector?

A vector is a list of numbers that can describe a quantity with size and direction.

For example:

`[4, 3]`

This vector has two components:
- `4` is the first component.
- `3` is the second component.

Because it has two components, it is a **two-dimensional (2D) vector**.

In Python, we can use a list to represent a vector:

```python
vector = [4, 3]
```

A Python list is only a way to store the numbers. Python does not automatically treat every list as a mathematical vector.

### 2. Direction

The signs of the components help describe the direction.

- `[4, 3]` and `[4, 3]` point in the same direction.
- `[4, 3]` and `[-4, -3]` point in opposite directions.

### 3. Magnitude

The **magnitude** of a vector means its length.

For a 2D vector `[x, y]`, use:

```text
magnitude = square root of (x squared + y squared)
```

In mathematical notation:

`|v| = √(x² + y²)`

Example with `[3, 4]`:

```text
|v| = √(3² + 4²)
    = √(9 + 16)
    = √25
    = 5
```

Another example:

```text
[5, 12] → √(25 + 144) → √169 → 13
```

### 4. Python implementation

The practical function is in [code/vector_magnitude.py](code/vector_magnitude.py).

The important Python parts are:

- `vector[0]` gets the first item in the list.
- `vector[1]` gets the second item.
- `**2` raises a number to the power of 2.
- `**0.5` raises a number to the power of one-half, which gives the square root for non-negative values.

The function currently handles **2D vectors** (lists containing two numbers).

### 5. Sample checks

The function was checked with these sample inputs in a Python execution environment:

| Input vector | Expected magnitude | Result |
|---|---:|---:|
| `[3, 4]` | 5 | 5.0 |
| `[6, 8]` | 10 | 10.0 |
| `[5, 12]` | 13 | 13.0 |

I ran the file successfully in my own local project workspace. It printed `5.0`, `10.0`, and `13.0`, matching the expected results.

### 6. What I learned

- A vector can be represented by its components.
- A vector with two components is 2D.
- Two vectors with the same components point in the same direction.
- Changing both component signs gives the opposite direction.
- Magnitude tells us the vector's length.
- The Pythagorean theorem helps us calculate the magnitude of a 2D vector.

### 7. Mistake and correction

I first gave `5.29` for the magnitude of `[6, 8]`. Working through the formula showed that the correct calculation is:

`√(6² + 8²) = √100 = 10`

This reminded me to square both components, add the results, and only then find the square root.

### 8. Learning checkpoint

- **Pre-lesson quiz:** 0/2. This was a starting-point check, not a final score.
- **Segment 1:** Understanding checks completed successfully after explanations and corrections.
- **Official lesson practical and post-lesson quiz:** Not yet completed.
- **Next:** Run `code/vector_magnitude.py` locally, then continue to vector addition and subtraction when ready.
