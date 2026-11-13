# Lesson 1: Linear Algebra Intuition

## Segment 1 — Vector basics and magnitude

**Status:** Segments 1 and 2 understood. Both the magnitude and vector-operations Python files were run successfully in my local environment.

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

## Segment 2 — Vector addition and subtraction

**Status:** Understanding confirmed. The Python implementation was run successfully in my local environment.

### 1. Vector addition

To add two vectors, add the components in matching positions.

Example:

`A = (6, 5)` and `B = (2, 3)`

```text
A + B = (6 + 2, 5 + 3)
      = (8, 8)
```

### 2. Vector subtraction

To subtract two vectors, subtract the second vector's components from the matching components of the first vector.

```text
A - B = (6 - 2, 5 - 3)
      = (4, 2)
```

A negative component is valid. For example, `(8, 4) - (5, 6) = (3, -2)`.

### 3. Python implementation

The practical function is in [code/vector_operations.py](code/vector_operations.py).

- `vector_a` and `vector_b` are parameters that receive the two input vectors.
- Python list indexing starts at zero: `vector_a[0]` accesses the first component and `vector_a[1]` accesses the second.
- The function adds or subtracts corresponding components and places the results in a new list.
- `return` sends that result back to the place where the function was called, so it can be stored or reused.

For example, `add_vectors([10, 4], [3, 8])` returns `[13, 12]`.

### 4. Local execution evidence

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/vector_operations.py
```

The program printed:

```text
Addition: [8, 8]
Subtraction: [4, 2]
```

Both results matched the expected calculations.

### 5. What I learned

- Addition combines corresponding components.
- Subtraction subtracts corresponding components.
- `[0]` means the first list element; `[1]` means the second.
- Function parameters receive the values supplied when a function is called.
- `return` makes a function's result available for later use.

### 6. Learning checkpoint

- **Segment 2:** Understanding checks completed successfully.
- **Python implementation:** Both functions ran locally with the expected output.
- **Official lesson practical and post-lesson quiz:** Not yet completed.

### 8. Learning checkpoint

- **Pre-lesson quiz:** 0/2. This was a starting-point check, not a final score.
- **Segment 1:** Understanding checks completed successfully after explanations and corrections.
- **Official lesson practical and post-lesson quiz:** Not yet completed.
- **Next:** Run `code/vector_magnitude.py` locally, then continue to vector addition and subtraction when ready.
