"""Official Practical 3: Find the most similar pair of random word-like vectors.

Create five 50-dimensional vectors, compare every unique pair with cosine
similarity, and report the pair with the highest score.
"""

import math
import random


def dot_product(vector_a, vector_b):
    """Return the sum of products of corresponding components."""
    return sum(a * b for a, b in zip(vector_a, vector_b))


def magnitude(vector):
    """Return the length of a vector."""
    return math.sqrt(sum(value ** 2 for value in vector))


def cosine_similarity(vector_a, vector_b):
    """Return cosine similarity for two nonzero vectors."""
    if len(vector_a) != len(vector_b):
        raise ValueError("Vectors must have the same number of dimensions.")

    # Cosine similarity compares direction, so use vector magnitudes to normalize.
    magnitude_a = magnitude(vector_a)
    magnitude_b = magnitude(vector_b)

    if magnitude_a == 0 or magnitude_b == 0:
        raise ValueError("Cosine similarity is undefined for a zero vector.")

    return dot_product(vector_a, vector_b) / (magnitude_a * magnitude_b)


if __name__ == "__main__":
    # A fixed seed makes the random vectors and result repeatable.
    random.seed(42)

    words = ["Apple", "Orange", "Banana", "Car", "Bus"]
    word_vectors = {}

    # Generate one 50-dimensional vector for each word.
    for word in words:
        word_vectors[word] = [
            random.uniform(-1, 1) for _ in range(50)
        ]

    # Convert the dictionary entries to a list so we can access them by index.
    word_items = list(word_vectors.items())

    # Cosine scores may be negative; begin lower than any possible score.
    highest_similarity = float("-inf")
    # No best pair has been selected yet.
    most_similar_pair = None

    # Compare every unique pair once; j starts at i + 1 to skip self-pairs
    # and avoid comparing the same pair again in reverse order.
    for i in range(len(word_items)):
        for j in range(i + 1, len(word_items)):
            name_a, vector_a = word_items[i]
            name_b, vector_b = word_items[j]

            similarity = cosine_similarity(vector_a, vector_b)
            print(f"{name_a} - {name_b}: {similarity:.4f}")

            # Replace the current best pair only when this score is higher.
            if similarity > highest_similarity:
                highest_similarity = similarity
                most_similar_pair = (name_a, name_b)

    print("\nMost similar pair:", most_similar_pair)
    print(f"Cosine similarity: {highest_similarity:.4f}")
