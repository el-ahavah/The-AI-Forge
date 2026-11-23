"""Official Practical 5: Create and verify a 3x3 matrix of rank 2.

The third row is the sum of the first two rows. Therefore, it does not
add a new independent direction, and the matrix has rank 2.

This practical calculates rank using Gaussian elimination and only
Python's standard library.
"""

TOLERANCE = 1e-10


def matrix_rank(matrix, tolerance=TOLERANCE):
    """Return the number of linearly independent rows using elimination."""
    rows = [row[:] for row in matrix]
    row_count = len(rows)
    column_count = len(rows[0])

    pivot_row = 0

    for column in range(column_count):
        # Find a non-zero pivot in this column.
        pivot = None
        for candidate_row in range(pivot_row, row_count):
            if abs(rows[candidate_row][column]) > tolerance:
                pivot = candidate_row
                break

        # No pivot in this column means it adds no new independent row.
        if pivot is None:
            continue

        # Move the pivot row into the current pivot position.
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]

        # Eliminate values below the pivot.
        pivot_value = rows[pivot_row][column]

        for current_row in range(pivot_row + 1, row_count):
            factor = rows[current_row][column] / pivot_value

            for current_column in range(column, column_count):
                rows[current_row][current_column] -= (
                    factor * rows[pivot_row][current_column]
                )

        pivot_row += 1

        if pivot_row == row_count:
            break

    return pivot_row


if __name__ == "__main__":
    matrix = [
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 2],
    ]

    print("Matrix:")
    for row in matrix:
        print(row)

    rank = matrix_rank(matrix)

    print("\nMatrix rank:", rank)
    print("Expected rank: 2")
    print("Rank verified:", rank == 2)

    print(
        "\nGeometric meaning: the columns span a plane through the origin "
        "in 3D space, because there are only two independent directions."
    )
