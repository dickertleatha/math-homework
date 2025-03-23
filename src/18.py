import numpy as np

def square_matrix(matrix):
    """
    This function takes a 2D matrix and returns its square version.
    The elements of the resulting matrix are square values of the original ones.
    """

    # Calculate the square value for each element in the matrix
    square_values = np.square(np.array(matrix))

    return square_values

# Example usage:
matrix = np.array([[1, 2], [3, 4]])
square_matrixed = square_matrix(matrix)
print(square_matrixed)
