"""Official Practical 1: Calculate the angle between two vectors.

Complete the angle_between method as part of the lesson exercise.
"""

import math


class Vector:
    def __init__(self, components):
        self.components = list(components)

    def dot(self, other):
        return sum(
            a * b
            for a, b in zip(self.components, other.components)
        )

    def magnitude(self):
        return sum(
            component ** 2
            for component in self.components
        ) ** 0.5

    def cosine_similarity(self, other):
        return self.dot(other) / (
            self.magnitude() * other.magnitude()
        )

    def angle_between(self, other):
        """Return the angle between this vector and another, in degrees."""
        cos_theta = self.cosine_similarity(other)
        cos_theta = max(-1.0, min(1.0, cos_theta))
        return math.degrees(math.acos(cos_theta))


if __name__ == "__main__":
    first = Vector([1, 0])
    perpendicular = Vector([0, 1])
    same_direction = Vector([1, 0])

    print(
        "Perpendicular vectors:",
        first.angle_between(perpendicular),
        "degrees",
    )
    print(
        "Same direction:",
        first.angle_between(same_direction),
        "degrees",
    )
