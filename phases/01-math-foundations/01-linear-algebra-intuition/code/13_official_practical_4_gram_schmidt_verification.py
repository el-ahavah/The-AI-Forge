"""Official Practical 4: Verify that Gram-Schmidt output is orthonormal.

Orthonormal means:
- Each vector has magnitude 1.
- The dot product of every pair of different vectors is 0.

This practical uses only Python's standard library.
"""

TOLERANCE = 1e-9


def dot_product(vector_a, vector_b):
    """Return the dot product of two vectors."""
    return sum(a * b for a, b in zip(vector_a, vector_b))


def magnitude(vector):
    """Return the length of a vector."""
    return sum(value ** 2 for value in vector) ** 0.5


def subtract_vectors(vector_a, vector_b):
    """Subtract corresponding components of two vectors."""
    return [a - b for a, b in zip(vector_a, vector_b)]


def project_onto(vector_a, vector_b):
    """Return the projection of vector_a onto vector_b."""
    denominator = dot_product(vector_b, vector_b)

    if denominator == 0:
        raise ValueError("Cannot project onto a zero vector.")

    scale = dot_product(vector_a, vector_b) / denominator
    return [scale * value for value in vector_b]


def normalize(vector):
    """Return a unit vector pointing in the same direction."""
    length = magnitude(vector)

    if length == 0:
        raise ValueError("Cannot normalize a zero vector.")

    return [value / length for value in vector]


def gram_schmidt(vectors):
    """Convert independent input vectors into an orthonormal set."""
    # Build the new orthonormal set one vector at a time.
    orthonormal_vectors = []

    for vector in vectors:
        # Make a copy so that the original input vector is not changed.
        remainder = vector[:]

        # Remove any part pointing along directions already in the set.
        for previous_unit_vector in orthonormal_vectors:
            projection = project_onto(remainder, previous_unit_vector)
            remainder = subtract_vectors(remainder, projection)

        if magnitude(remainder) < TOLERANCE:
            raise ValueError("The input vectors are linearly dependent.")

        # Normalize what remains so its length becomes exactly 1.
        orthonormal_vectors.append(normalize(remainder))

    return orthonormal_vectors


def verify_orthonormal(vectors, tolerance=TOLERANCE):
    """Check unit magnitudes and zero pairwise dot products."""
    # Both conditions must be true for the set to be orthonormal.
    all_unit_length = True
    all_perpendicular = True

    for index, vector in enumerate(vectors):
        length = magnitude(vector)
        is_unit = abs(length - 1.0) < tolerance
        print(f"Vector {index + 1}: {vector}")
        print(f"  Magnitude: {length:.6f} (unit length: {is_unit})")

        if not is_unit:
            all_unit_length = False

    # Check each distinct pair once.
    for i in range(len(vectors)):
        for j in range(i + 1, len(vectors)):
            product = dot_product(vectors[i], vectors[j])
            is_perpendicular = abs(product) < tolerance
            print(
                f"Vector {i + 1} · Vector {j + 1}: "
                f"{product:.6f} (perpendicular: {is_perpendicular})"
            )

            if not is_perpendicular:
                all_perpendicular = False

    return all_unit_length and all_perpendicular


if __name__ == "__main__":
    input_vectors = [
        [1, 0, 0],
        [1, 1, 0],
        [1, 1, 1],
    ]

    print("Input vectors:", input_vectors)

    orthonormal_vectors = gram_schmidt(input_vectors)

    print("\nGram-Schmidt output:")
    is_orthonormal = verify_orthonormal(orthonormal_vectors)

    print("\nAre the vectors orthonormal?", is_orthonormal)
