"""Apply a 2D scaling matrix to a vector."""


def matrix_vector_multiply(matrix, vector):
    """Multiply a matrix by a vector and return the resulting vector."""
    if not matrix:
        raise ValueError("The matrix must contain at least one row.")

    number_of_columns = len(matrix[0])

    if any(len(row) != number_of_columns for row in matrix):
        raise ValueError("Every matrix row must have the same number of columns.")

    if number_of_columns != len(vector):
        raise ValueError("The matrix columns must match the vector components.")

    result = []

    for row in matrix:
        total = 0

        for column_index in range(number_of_columns):
            total += row[column_index] * vector[column_index]

        result.append(total)

    return result


if __name__ == "__main__":
    # Double the x-coordinate and triple the y-coordinate.
    scaling_matrix = [
        [2, 0],
        [0, 3],
    ]

    original_vector = [1, 1]
    transformed_vector = matrix_vector_multiply(
        scaling_matrix,
        original_vector,
    )

    print("Original vector:", original_vector)
    print("Scaling matrix:", scaling_matrix)
    print("Transformed vector:", transformed_vector)
