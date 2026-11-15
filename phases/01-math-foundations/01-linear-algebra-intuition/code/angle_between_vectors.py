"""Calculate the angle between two vectors in degrees."""

from math import acos, degrees, sqrt


def angle_between_vectors(vector_a, vector_b):
    """Return the angle between two nonzero vectors, in degrees."""
    if len(vector_a) != len(vector_b):
        raise ValueError("Both vectors must have the same number of components.")

    dot_product = sum(
        a * b for a, b in zip(vector_a, vector_b)
    )

    magnitude_a = sqrt(sum(component ** 2 for component in vector_a))
    magnitude_b = sqrt(sum(component ** 2 for component in vector_b))

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("The angle is undefined for a zero vector.")

    cosine = dot_product / (magnitude_a * magnitude_b)

    # Keep the value inside [-1, 1] to avoid floating-point errors.
    cosine = max(-1.0, min(1.0, cosine))

    return degrees(acos(cosine))


if __name__ == "__main__":
    first = [1, 0]
    perpendicular = [0, 1]
    opposite = [-1, 0]

    print("Same direction:", angle_between_vectors(first, first), "degrees")
    print("Perpendicular:", angle_between_vectors(first, perpendicular), "degrees")
    print("Opposite direction:", angle_between_vectors(first, opposite), "degrees")
