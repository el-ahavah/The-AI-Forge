"""Official Practical 6: Project a vector onto another vector.

Project [1, 2, 3] onto [1, 1, 1], then verify that the remainder
is perpendicular to the direction vector.
"""


def dot(vector_a, vector_b):
    """Calculate the dot product of two vectors."""
    return sum(a * b for a, b in zip(vector_a, vector_b))


def project_onto(vector_a, vector_b):
    """Return the projection of vector_a onto the direction vector_b."""
    # This is the squared length of the direction vector.
    denominator = dot(vector_b, vector_b)

    if denominator == 0:
        raise ValueError("Cannot project onto a zero vector.")

    # Calculate how much of vector_a points along vector_b.
    scale = dot(vector_a, vector_b) / denominator
    return [scale * component for component in vector_b]


def subtract_vectors(vector_a, vector_b):
    """Subtract matching components of two vectors."""
    return [a - b for a, b in zip(vector_a, vector_b)]


if __name__ == "__main__":
    vector_a = [1, 2, 3]
    vector_b = [1, 1, 1]

    # Projection is the part along vector_b; subtract to find the leftover.
    projection = project_onto(vector_a, vector_b)
    remainder = subtract_vectors(vector_a, projection)

    print("Vector being projected:", vector_a)
    print("Direction vector:", vector_b)
    print("Projection:", projection)
    print("Remainder:", remainder)
    # If this dot product is zero, the leftover is perpendicular to vector_b.
    print("Remainder dot direction:", dot(remainder, vector_b))
    print(
        "Remainder is perpendicular:",
        dot(remainder, vector_b) == 0,
    )
