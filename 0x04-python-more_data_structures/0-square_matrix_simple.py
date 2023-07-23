#!/usr/bin/python3
def square_matrix(x):
    return x ** 2


def square_matrix_simple(matrix=[]):
    # Use lambda to compute square of each element in the matrix
    # square_matrix = lambda x: x ** 2
    # Create a new matrix to store the squared values
    new_matrix = []
    # Use map to apply the square_matrix
    # function to each element in the matrix
    for row in matrix:
        new_row = list(map(square_matrix, row))
        new_matrix.append(new_row)
    return new_matrix
