# Lesson 1: Linear Algebra Intuition

## Segment 1 — Vector basics and magnitude

**Status:** Segments 1–4 understood. The magnitude, vector-operations, and scalar-multiplication Python files were run successfully in my local environment.

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

### 6. Segment 2 checkpoint

- **Segment 2:** Understanding checks completed successfully.
- **Python implementation:** Both functions ran locally with the expected output.
- **Official lesson practical and post-lesson quiz:** Not yet completed.

## Segment 3 — Scalar multiplication

**Status:** Understanding checks completed successfully. The Python implementation ran locally and produced the expected results.

### 1. What is scalar multiplication?

A scalar is a single number. Scalar multiplication means multiplying every component of a vector by that number.

For example, if:

`A = (4, 5)`

Then:

- `2A = (2 × 4, 2 × 5) = (8, 10)`
- `3A = (3 × 4, 3 × 5) = (12, 15)`
- `-1A = (-1 × 4, -1 × 5) = (-4, -5)`

A positive scalar changes the vector's length while keeping its direction. A negative scalar also reverses its direction.

### 2. Python implementation

The practical function is in [code/vector_scalar_multiplication.py](code/vector_scalar_multiplication.py).

- `vector` receives the vector.
- `scalar` receives the number to multiply by.
- `vector[0] * scalar` multiplies the first component.
- `vector[1] * scalar` multiplies the second component.
- The function returns both results as a new list.

### 3. Local execution evidence

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/vector_scalar_multiplication.py
```

The program printed:

```text
[8, 10]
[12, 15]
[-4, -5]
```

All three outputs matched the expected calculations.

### 4. What I learned

- A scalar is one number.
- Scalar multiplication applies the same scalar to every component of a vector.
- A positive scalar keeps the direction; a negative scalar reverses it.
- Each vector component is multiplied separately, and the results together form the new vector.

### 5. Segment 3 checkpoint

- **Understanding checks:** All three answers were correct.
- **Python implementation:** Ran locally with the expected output.

## Segment 4 — Dot product

**Status:** Understanding checks completed successfully. The Python implementation ran locally and produced the expected positive, negative, and zero results.

### 1. What is the dot product?

The dot product combines two vectors into one number (a scalar). Multiply the components in matching positions, then add those products.

For two 2D vectors:

`A · B = (a1 × b1) + (a2 × b2)`

Example:

`A = [2, 3]` and `B = [4, 1]`

```text
(2 × 4) + (3 × 1)
= 8 + 3
= 11
```

### 2. What the result tells us about direction

For two nonzero vectors:
- A positive dot product means the angle between them is less than 90 degrees; they point generally in the same direction.
- A negative dot product means the angle is greater than 90 degrees; they point generally in opposite directions.
- A zero dot product means they are perpendicular (90 degrees apart).

A negative result does not always mean the vectors are exact reverses. In the example `[2, 3]` and `[-2, -3]`, they are exact opposites because one is the negative of the other.

### 3. Python implementation

The practical function is in [code/dot_product.py](code/dot_product.py).

- `vector_a[0] * vector_b[0]` multiplies the first components.
- `vector_a[1] * vector_b[1]` multiplies the second components.
- The function adds both products and returns one number.

### 4. Local execution evidence

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/dot_product.py
```

The program printed:

```text
Positive dot product: 11
Negative dot product: -13
Zero dot product: 0
```

All three results matched the expected calculations.

### 5. What I learned

- The dot product multiplies matching components and adds the products.
- Its result is a scalar, not a vector.
- The sign of the dot product tells us whether the angle is acute, obtuse, or (for a zero result) right.
- A zero dot product means perpendicular vectors when both vectors are nonzero.

### 6. Segment 4 checkpoint

- **Understanding checks:** Correctly calculated positive (23), negative (-13), and zero (0) dot products and identified the perpendicular relationship in the zero-result example.
- **Python implementation:** Ran locally with all three expected outputs.
- **Official lesson practical and post-lesson quiz:** Not yet completed.

### 7. Overall lesson checkpoint

- **Pre-lesson quiz:** 0/2. This was a starting-point check, not a final score.
- **Segment 1:** Understanding checks completed successfully after explanations and corrections.
- **Segment 2:** Understanding checks completed successfully; vector addition and subtraction ran locally.
- **Segment 3:** Understanding checks completed successfully; scalar multiplication ran locally with outputs `[8, 10]`, `[12, 15]`, and `[-4, -5]`.
- **Segment 4:** Dot product understanding checks completed successfully; `dot_product.py` ran locally with outputs `11`, `-13`, and `0`.
- **Official lesson practical and post-lesson quiz:** Not yet completed.
- **Next:** Continue with the remaining concepts in the official lesson after the required practical and quiz work.
