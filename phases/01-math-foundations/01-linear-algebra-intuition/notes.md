# Lesson 1: Linear Algebra Intuition

## Segment 1 — Vector basics and magnitude

**Status:** Segments 1–9 have been covered through guided explanations and checks, and their local practicals have run successfully. Official Practical 1 (angle between vectors) has also been completed and run locally; Official Practical 1 (angle between vectors) and Official Practical 2 (2D scaling matrix) are complete and run locally; Official Practicals 3–6 and the post-lesson quiz remain pending.

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

The practical function is in [code/1_vector_magnitude.py](code/1_vector_magnitude.py).

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

The practical function is in [code/2_vector_operations.py](code/2_vector_operations.py).

- `vector_a` and `vector_b` are parameters that receive the two input vectors.
- Python list indexing starts at zero: `vector_a[0]` accesses the first component and `vector_a[1]` accesses the second.
- The function adds or subtracts corresponding components and places the results in a new list.
- `return` sends that result back to the place where the function was called, so it can be stored or reused.

For example, `add_vectors([10, 4], [3, 8])` returns `[13, 12]`.

### 4. Local execution evidence

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/2_vector_operations.py
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

The practical function is in [code/3_vector_scalar_multiplication.py](code/3_vector_scalar_multiplication.py).

- `vector` receives the vector.
- `scalar` receives the number to multiply by.
- `vector[0] * scalar` multiplies the first component.
- `vector[1] * scalar` multiplies the second component.
- The function returns both results as a new list.

### 3. Local execution evidence

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/3_vector_scalar_multiplication.py
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

The practical function is in [code/4_dot_product.py](code/4_dot_product.py).

- `vector_a[0] * vector_b[0]` multiplies the first components.
- `vector_a[1] * vector_b[1]` multiplies the second components.
- The function adds both products and returns one number.

### 4. Local execution evidence

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/4_dot_product.py
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
- **Segment 4:** Dot product understanding checks completed successfully; `4_dot_product.py` ran locally with outputs `11`, `-13`, and `0`.
- **Official lesson practical and post-lesson quiz:** Not yet completed.
- **Next:** Continue with the remaining concepts in the official lesson after the required practical and quiz work.


## Segment 5 — Vector normalization

**Status:** Conceptual understanding confirmed. The Python practical has been created; local execution is pending.

### 1. What is normalization?

Normalization changes a vector's length to 1 while keeping its direction the same. A vector with length 1 is called a **unit vector**.

To normalize a vector, divide every component by the vector's magnitude.

### 2. Example

For the vector `[6, 8]`:

```text
Magnitude = √(6² + 8²) = √100 = 10

Normalized vector = [6 ÷ 10, 8 ÷ 10]
                  = [0.6, 0.8]
```

The new vector points in the same direction, but its length is 1.

### 3. Why it matters in AI

Normalizing embedding vectors can make comparisons focus on direction rather than differences in vector length. This is useful in similarity-based tasks such as semantic search.

### 4. Python implementation

The practical is in [code/5_vector_normalization.py](code/5_vector_normalization.py).

- `hypot(x, y)` calculates the vector's magnitude.
- Each component is divided by that magnitude.
- The function returns a new list, leaving the original vector unchanged.
- A zero vector has magnitude 0, so division would be impossible. The function raises a clear `ValueError` for that case.

### 5. Local execution evidence

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/5_vector_normalization.py
```

The program printed:

```text
Original vector: [6, 8]
Normalized vector: [0.6, 0.8]
```

The output matched the expected normalized vector.

### 6. Segment 5 checkpoint

- **Understanding check:** Correctly normalized `[6, 8]` to `[0.6, 0.8]`.
- **Python practical:** Ran locally and produced the expected output.
- **Official lesson practical and post-lesson quiz:** Still pending.

## Segment 6 — Cosine similarity

**Status:** Conceptual understanding confirmed. The Python practical was run locally and produced the expected output.

### 1. What does cosine similarity measure?

Cosine similarity measures how closely two nonzero vectors point in the same direction. It focuses on direction rather than the vectors' lengths.

Its value ranges from -1 to 1:

- `1`: same direction.
- `0`: perpendicular directions.
- `-1`: opposite directions.

### 2. Formula

```text
cosine similarity = (A · B) / (|A| × |B|)
```

This means: divide the dot product by the product of the two vector magnitudes.

### 3. Example

For `A = [1, 0]` and `B = [2, 0]`:

```text
Dot product = (1 × 2) + (0 × 0) = 2
Magnitude of A = 1
Magnitude of B = 2

Cosine similarity = 2 / (1 × 2) = 1
```

The result is 1 because both vectors point in exactly the same direction, even though their lengths are different.

### 4. Why it matters in AI

Cosine similarity is commonly used to compare embedding vectors, for example when searching for text or items with related meanings. It helps compare their directions without letting vector length directly determine the similarity score.

### 5. Python implementation

The practical is in [code/6_cosine_similarity.py](code/6_cosine_similarity.py).

- The function calculates the dot product of the two vectors.
- `hypot()` calculates each vector's magnitude.
- It divides the dot product by the product of the magnitudes.
- A zero vector cannot be used because its magnitude would make the denominator zero. The function raises a clear `ValueError` in that case.

### 6. Local execution evidence

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/6_cosine_similarity.py
```

The program printed:

```text
Same direction: 1.0
Perpendicular: 0.0
Opposite directions: -1.0
```

All three results matched the expected cosine similarity values.

### 7. Segment 6 checkpoint

- **Understanding check:** Correctly calculated a cosine similarity of `1` for `[1, 0]` and `[2, 0]`.
- **Python practical:** Ran locally and produced the expected outputs for same, perpendicular, and opposite directions.
- **Official lesson practical and post-lesson quiz:** Still pending.

## Updated lesson checkpoint

- **Pre-lesson quiz:** 0/2 (baseline check).
- **Segments 1–4:** Understanding checks completed; the four Python files for magnitude, vector operations, scalar multiplication, and dot product were run locally with expected outputs.
- **Segment 5:** Normalization understood; `5_vector_normalization.py` ran locally and produced `[0.6, 0.8]`.
- **Segment 6:** Cosine similarity understood; `6_cosine_similarity.py` ran locally and produced `1.0`, `0.0`, and `-1.0`.
- **Segment 7:** Angles between vectors covered; `code/7_angle_between_vectors.py` created and committed. Local execution is pending.
- **Segment 8:** Matrix-vector multiplication and scaling covered; `code/8_matrix_vector_multiplication.py` created and committed. Local execution is pending.
- **Official lesson practical and post-lesson quiz:** Not yet completed.


## Segment 7 — Angles between vectors

**Status:** The concept has been introduced and the Python practical has been created and committed. Local execution is pending.

### 1. What is the angle between vectors?

The angle between two nonzero vectors describes how far apart their directions are.

- **0°:** They point in the same direction.
- **90°:** They are perpendicular.
- **180°:** They point in opposite directions.

### 2. How do we calculate the angle?

We use the dot product and the magnitudes of both vectors:

```text
cos(angle) = (A · B) / (|A| × |B|)
angle = arccos(cos(angle))
```

The inverse cosine (`acos`) gives an angle in radians; Python's `degrees()` converts it to degrees.

For example, `A = [1, 0]` and `B = [0, 1]` have a dot product of 0, so their angle is 90°.

### 3. Python implementation

The practical is in [code/7_angle_between_vectors.py](code/7_angle_between_vectors.py).

- The function checks that both vectors have the same number of components.
- It calculates their dot product and magnitudes.
- It divides the dot product by the product of the magnitudes.
- It clamps the cosine value to the range -1 to 1 to protect against small floating-point rounding errors.
- `acos()` and `degrees()` convert that value into an angle in degrees.
- A zero vector is rejected because its angle is undefined.

### 4. Local execution

Local execution was completed successfully with:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/7_angle_between_vectors.py
```

I ran the file locally. It printed `Same direction: 0.0 degrees`, `Perpendicular: 90.0 degrees`, and `Opposite direction: 180.0 degrees`. All three outputs matched the expected angles.

### 5. Segment 7 checkpoint

- **Understanding check:** Correctly identified 0° for vectors pointing in the same direction; the opposite-direction check was used to reinforce the 180° case.
- **Python practical:** Ran locally and produced 0°, 90°, and 180° for same, perpendicular, and opposite directions.

## Segment 8 — Matrix transformations and scaling

**Status:** The matrix-vector multiplication concept and Python implementation have been covered step by step. The practical ran successfully in the local environment.

### 1. What is a matrix transformation?

A matrix is a rectangular arrangement of numbers. When we multiply a matrix by a vector, the matrix transforms that vector into a new vector.

A transformation can stretch, shrink, rotate, or otherwise change a vector.

### 2. Scaling with a matrix

To double the x-coordinate and triple the y-coordinate, use this matrix:

```text
[2  0]
[0  3]
```

Apply it to `[1, 1]`:

```text
[2  0]   [1]   [2×1 + 0×1]   [2]
[0  3] × [1] = [0×1 + 3×1] = [3]
```

The transformed vector is `[2, 3]`.

The diagonal values control the scaling of each coordinate. The zeros mean the x-coordinate does not contribute to the new y-coordinate, and the y-coordinate does not contribute to the new x-coordinate.

### 3. Python implementation

The practical is in [code/8_matrix_vector_multiplication.py](code/8_matrix_vector_multiplication.py).

- The function checks that the matrix is not empty.
- It checks that all rows have the same number of columns.
- It checks that the vector length matches the number of matrix columns.
- For each row, it multiplies each matrix value by the matching vector component and adds the products.
- The results form the transformed vector.

### 4. Local execution

Local execution is pending. After pulling the latest changes, run:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/8_matrix_vector_multiplication.py
```

I ran the file locally. It printed the original vector `[1, 1]`, the scaling matrix `[[2, 0], [0, 3]]`, and the transformed vector `[2, 3]`. The output matched the expected matrix transformation.

### 5. Segment 8 checkpoint

- **Matrix transformation:** The idea of applying a matrix to change a vector has been introduced.
- **Python practical:** Ran locally and transformed `[1, 1]` into `[2, 3]` using the scaling matrix.

## Updated lesson checkpoint

- **Pre-lesson quiz:** 0/2 (baseline check).
- **Segments 1–4:** Understanding checks completed; the four Python files for magnitude, vector operations, scalar multiplication, and dot product were run locally with expected outputs.
- **Segment 5:** Normalization practical ran locally and produced `[0.6, 0.8]`.
- **Segment 6:** Cosine similarity practical ran locally and produced `1.0`, `0.0`, and `-1.0`.
- **Segment 7:** `7_angle_between_vectors.py` ran locally and returned 0.0°, 90.0°, and 180.0° for same, perpendicular, and opposite directions.
- **Segment 8:** `8_matrix_vector_multiplication.py` ran locally and transformed `[1, 1]` into `[2, 3]`.
- **Official lesson practical and post-lesson quiz:** Not yet completed.


## Segment 9 — Linear independence

**Status:** Guided explanation and understanding checks completed. The practical ran successfully in the local environment.

### 1. What does linear independence mean?

A set of vectors is **linearly independent** when none of its vectors can be made by combining the other vectors.

A set is **linearly dependent** when at least one vector can be made by combining the others.

### 2. Example of dependent vectors

Consider these three vectors:

```text
v1 = [1, 0, 0]
v2 = [0, 1, 0]
v3 = [2, 1, 0]
```

The third vector can be made by doubling the first vector and adding the second:

```text
2 × v1 + v2
= [2, 0, 0] + [0, 1, 0]
= [2, 1, 0]
= v3
```

Because one vector can be made from the other two, this set is **linearly dependent**.

Notice that all three vectors have a third component of zero. They lie on the same flat plane (the xy-plane), so they do not provide three independent directions in 3D space.

### 3. Python practical

The demonstration is in [code/9_linear_independence.py](code/9_linear_independence.py).

- `scale_vector()` multiplies every component by a number.
- `add_vectors()` adds matching components from two vectors.
- The main example calculates `2 * v1 + v2` and compares the result with `v3`.
- If the two lists are equal, the example confirms that `v3` can be made from `v1` and `v2`.

This file demonstrates one dependent set. It is not yet a general-purpose algorithm for testing every possible set of vectors.

### 4. Local execution

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/9_linear_independence.py
```

The program printed:

```text
2 * vector_1 + vector_2: [2, 1, 0]
vector_3: [2, 1, 0]
The set is linearly dependent: True
All three vectors have a z-coordinate of 0.
They lie in the xy-plane, not throughout 3D space.
```

The combined vector matched `vector_3`, confirming that the set is linearly dependent. The final two lines show that all three vectors lie in the xy-plane because their third components are zero.

### 5. Segment 9 checkpoint

- **Concept:** Explained linear independence and dependence; understanding checks completed successfully.
- **Python practical:** Ran locally and confirmed `2 * vector_1 + vector_2` equals `vector_3`.
- **Geometric observation:** All three vectors have a zero z-coordinate and lie in the xy-plane.


## Official Practical 1 — Angle between vectors

**Status:** Completed, pulled from GitHub, and run successfully in the local environment.

The official practical extends the `Vector` class with an `angle_between(other)` method. It reuses cosine similarity to obtain the cosine of the angle, clamps the value to the valid range from -1 to 1 to protect against floating-point rounding, then uses `math.acos()` and `math.degrees()` to return the angle in degrees.

The implementation is in [code/10_official_practical_1_angle_between_vectors.py](code/10_official_practical_1_angle_between_vectors.py).

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/10_official_practical_1_angle_between_vectors.py
```

It printed:

```text
Perpendicular vectors: 90.0 degrees
Same direction: 0.0 degrees
```

Both results matched the expected values. The implementation was committed to GitHub, pulled, and then verified by running it locally.

**Next:** Official Practicals 2–6, followed by the official post-lesson quiz.


## Official Practical 2 — 2D scaling matrix

**Status:** Completed, pulled from GitHub, and run successfully in the local environment.

The task was to create a 2D scaling matrix that doubles the x-coordinate and triples the y-coordinate, then apply it to the vector `[1, 1]`.

The scaling matrix is:

```text
[2  0]
[0  3]
```

The zeros prevent the coordinates from affecting each other. The first row calculates the new x-coordinate, and the second row calculates the new y-coordinate:

```text
(2 × 1) + (0 × 1) = 2
(0 × 1) + (3 × 1) = 3
```

The transformed vector is `[2, 3]`.

The implementation is in [code/11_official_practical_2_scaling_matrix.py](code/11_official_practical_2_scaling_matrix.py). It uses a row-by-row matrix-vector multiplication function: for each row, it multiplies matching components, adds the products, and appends the resulting component.

I ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/11_official_practical_2_scaling_matrix.py
```

It printed:

```text
Scaling matrix: [[2, 0], [0, 3]]
Original vector: [1, 1]
Transformed vector: [2, 3]
```

The output matched the expected result. The file was committed to GitHub, pulled, and verified by running it locally.

**Next:** Official Practicals 3–6, followed by the official post-lesson quiz.


### Official Practical 3 — Most similar word-like vectors

**Date:** 2026-11-20  
**Status:** Completed, committed, pulled, and run locally on 2026-11-20.

**Local execution evidence:** Ran:

```bash
python3 phases/01-math-foundations/01-linear-algebra-intuition/code/12_official_practical_3_most_similar_vectors.py
```

The program printed all 10 unique pair scores and identified `('Banana', 'Bus')` as the most similar pair, with cosine similarity `0.2963`. The output confirms that the program generated and compared the five vectors successfully.

**Official task:** Generate five random word-like vectors, each with 50 dimensions, compare every unique pair using cosine similarity, and identify the pair with the highest score.

**What I learned while preparing the implementation:**

- Five vectors contain 250 numerical components altogether (5 × 50), with 50 components in each vector.
- A dictionary maps each word name to its vector, so I can identify the vectors by their keys.
- A list comprehension such as `[random.uniform(-1, 1) for _ in range(50)]` generates 50 random numbers and collects them into a list.
- Five different vectors produce 10 unique pairs. Starting the inner loop at `i + 1` avoids comparing a vector with itself and avoids checking each pair twice in reverse order.
- The program keeps the best score in `highest_similarity` and the corresponding words in `most_similar_pair`. Both are updated only when a higher score is found.
- `random.seed(42)` makes the generated vectors repeatable between runs.

**Artifact:** [`12_official_practical_3_most_similar_vectors.py`](code/12_official_practical_3_most_similar_vectors.py).

**Next:** Complete Official Practicals 4–6 and the post-lesson quiz.
