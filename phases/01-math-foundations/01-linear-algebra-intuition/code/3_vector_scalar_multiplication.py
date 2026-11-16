"""Beginner-friendly scalar multiplication for 2D vectors."""


def multiply_vector(vector, scalar):
    """Return a new 2D vector with each component multiplied by scalar."""
    return [
        vector[0] * scalar,
        vector[1] * scalar,
    ]


if __name__ == "__main__":
    vector = [4, 5]

    print(multiply_vector(vector, 2))
    print(multiply_vector(vector, 3))
    print(multiply_vector(vector, -1))
