"""Official Practical 2: Apply a 2D scaling matrix to a vector.

The matrix doubles the x-coordinate and triples the y-coordinate.
"""


def matrix_vector_multiply(matrix, vector):
    """Multiply each matrix row by the vector to get the transformed vector."""
    result = []

    for row in matrix:
        total = 0

        for matrix_value, vector_value in zip(row, vector):
            total += matrix_value * vector_value

        result.append(total)

    return result


if __name__ == "__main__":
    scaling_matrix = [
        [2, 0],
        [0, 3],
    ]
    original_vector = [1, 1]

    transformed_vector = matrix_vector_multiply(
        scaling_matrix,
        original_vector,
    )

    print("Scaling matrix:", scaling_matrix)
    print("Original vector:", original_vector)
    print("Transformed vector:", transformed_vector)
