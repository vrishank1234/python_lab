def add_matrices(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Error: Matrices must have the same dimensions for addition.")
        return None

    # Add corresponding elements of the two matrices
    result_matrix = [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

    return result_matrix

# Example matrices
matrix_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix_b = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Add the matrices
result = add_matrices(matrix_a, matrix_b)

# Print the result
if result is not None:
    print("Matrix A:")
    [print(row) for row in matrix_a]

    print("\nMatrix B:")
    [print(row) for row in matrix_b]

    print("\nSum of Matrices A and B:")
    [print(row) for row in result]
