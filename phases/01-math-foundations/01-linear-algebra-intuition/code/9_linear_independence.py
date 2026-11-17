"""Demonstrate linear dependence with a simple vector combination."""


def scale_vector(vector, scalar):
    """Multiply every component of a vector by the same number."""
    return [component * scalar for component in vector]


def add_vectors(vector_a, vector_b):
    """Add two vectors by adding their matching components."""
    if len(vector_a) != len(vector_b):
        raise ValueError("Both vectors must have the same number of components.")

    return [
        vector_a[index] + vector_b[index]
        for index in range(len(vector_a))
    ]


if __name__ == "__main__":
    # These vectors are examples from the lesson.
    vector_1 = [1, 0, 0]
    vector_2 = [0, 1, 0]
    vector_3 = [2, 1, 0]

    # Check whether vector_3 can be made from vector_1 and vector_2.
    combination = add_vectors(
        scale_vector(vector_1, 2),
        vector_2,
    )

    print("2 * vector_1 + vector_2:", combination)
    print("vector_3:", vector_3)
    print("The set is linearly dependent:", combination == vector_3)
    print("All three vectors have a z-coordinate of 0.")
    print("They lie in the xy-plane, not throughout 3D space.")
