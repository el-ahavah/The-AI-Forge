"""Beginner-friendly normalization for a 2D vector."""

from math import hypot


def normalize_vector(vector):
    """Return a unit vector in the same direction as a nonzero 2D vector."""
    magnitude = hypot(vector[0], vector[1])

    if magnitude == 0:
        raise ValueError("The zero vector cannot be normalized.")

    return [
        vector[0] / magnitude,
        vector[1] / magnitude,
    ]


if __name__ == "__main__":
    vector = [6, 8]
    print("Original vector:", vector)
    print("Normalized vector:", normalize_vector(vector))
