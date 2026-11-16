"""Beginner-friendly 2D vector addition and subtraction."""


def add_vectors(vector_a, vector_b):
    """Return the sum of two 2D vectors."""
    return [
        vector_a[0] + vector_b[0],
        vector_a[1] + vector_b[1],
    ]


def subtract_vectors(vector_a, vector_b):
    """Return the difference between two 2D vectors."""
    return [
        vector_a[0] - vector_b[0],
        vector_a[1] - vector_b[1],
    ]


if __name__ == "__main__":
    vector_a = [6, 5]
    vector_b = [2, 3]

    print("Addition:", add_vectors(vector_a, vector_b))
    print("Subtraction:", subtract_vectors(vector_a, vector_b))
