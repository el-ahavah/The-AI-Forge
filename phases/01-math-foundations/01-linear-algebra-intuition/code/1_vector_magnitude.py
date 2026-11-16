"""A beginner-friendly function for finding the magnitude of a 2D vector."""


def magnitude(vector):
    """Return the length of a 2D vector.

    The vector must contain exactly two numbers: [x, y].
    """
    x = vector[0]
    y = vector[1]

    return (x**2 + y**2)**0.5


if __name__ == "__main__":
    # Sample checks: the expected answers are 5.0, 10.0, and 13.0.
    print(magnitude([3, 4]))
    print(magnitude([6, 8]))
    print(magnitude([5, 12]))
