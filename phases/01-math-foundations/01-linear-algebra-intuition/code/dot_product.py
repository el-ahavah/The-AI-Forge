"""Beginner-friendly dot product for two 2D vectors."""


def dot_product(vector_a, vector_b):
    """Return the dot product of two 2D vectors as a single number."""
    first_product = vector_a[0] * vector_b[0]
    second_product = vector_a[1] * vector_b[1]

    return first_product + second_product


if __name__ == "__main__":
    # Positive result: the vectors point generally in the same direction.
    vector_a = [2, 3]
    vector_b = [4, 1]
    print("Positive dot product:", dot_product(vector_a, vector_b))

    # Negative result: these vectors point in opposite directions.
    vector_c = [2, 3]
    vector_d = [-2, -3]
    print("Negative dot product:", dot_product(vector_c, vector_d))

    # Zero result: these nonzero vectors are perpendicular.
    vector_e = [2, 3]
    vector_f = [3, -2]
    print("Zero dot product:", dot_product(vector_e, vector_f))
