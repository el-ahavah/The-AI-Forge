"""Beginner-friendly cosine similarity for two 2D vectors."""

from math import hypot


def cosine_similarity(vector_a, vector_b):
    """Return how closely two nonzero 2D vectors point in the same direction."""
    dot_product = (
        vector_a[0] * vector_b[0]
        + vector_a[1] * vector_b[1]
    )

    magnitude_a = hypot(vector_a[0], vector_a[1])
    magnitude_b = hypot(vector_b[0], vector_b[1])

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector.")

    return dot_product / (magnitude_a * magnitude_b)


if __name__ == "__main__":
    vector_a = [1, 0]
    vector_b = [2, 0]
    print("Same direction:", cosine_similarity(vector_a, vector_b))

    vector_c = [1, 0]
    vector_d = [0, 1]
    print("Perpendicular:", cosine_similarity(vector_c, vector_d))

    vector_e = [1, 0]
    vector_f = [-2, 0]
    print("Opposite directions:", cosine_similarity(vector_e, vector_f))
