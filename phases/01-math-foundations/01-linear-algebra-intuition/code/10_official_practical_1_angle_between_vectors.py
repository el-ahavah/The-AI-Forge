"""Official Practical 1: Calculate angles between vectors.

This practical uses the dot product and cosine similarity to find
the angle between two vectors, in degrees.
"""

import math


class Vector:
    """A vector represented by a list of coordinates."""

    def __init__(self, components):
        self.components = list(components)

    def dot(self, other):
        """Multiply matching coordinates and add the products."""
        return sum(
            a * b
            for a, b in zip(self.components, other.components)
        )

    def magnitude(self):
        """Return the length of this vector."""
        return math.sqrt(
            sum(component ** 2 for component in self.components)
        )

    def cosine_similarity(self, other):
        """Compare the directions of two vectors."""
        denominator = self.magnitude() * other.magnitude()

        if denominator == 0:
            raise ValueError("Cosine similarity is undefined for a zero vector.")

        return self.dot(other) / denominator

    def angle_between(self, other):
        """Return the angle between two vectors, in degrees."""
        # Keep the cosine value within acos's valid range.
        cosine = max(-1.0, min(1.0, self.cosine_similarity(other)))

        # acos returns radians, so convert the answer to degrees.
        return math.degrees(math.acos(cosine))


if __name__ == "__main__":
    first = Vector([1, 0])
    perpendicular = Vector([0, 1])
    same_direction = Vector([1, 0])

    print("Perpendicular vectors:", first.angle_between(perpendicular), "degrees")
    print("Same direction:", first.angle_between(same_direction), "degrees")
