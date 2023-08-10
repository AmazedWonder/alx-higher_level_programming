#!/usr/bin/python3
"""Deefines class matrix.

Function that divides all elements of a matrix.
Matrix is a list of lists of integers or floats, otherwise
raise a TypeError exception.
Each row of the matrix is of the same size, otherwise
raise a TypeError exception.
Div is a number (integer or float), otherwise raise a TypeError exception
div shouldn't be equal to 0, otherwise raise a ZeroDivisionError exception
All elements of the matrix are divided by div, rounded to 2 decimal places

"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.

    Args:
        matrix (list): A matrix represented as a list of lists
        of integers or floats.
        div (number): The divisor (integer or float) used for division.

    Returns:
        list: A new matrix with elements divided by the divisor and
        rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a matrix (list of lists)
        of integers/floats,
                   if each row of the matrix does not have the same size,
                   or if the divisor is not a number.
        ZeroDivisionError: If the divisor is zero.

    Examples:
        >>> matrix = [[1, 2, 3], [4, 5, 6]]
        >>> divisor = 2
        >>> result = matrix_divided(matrix, divisor)
        >>> print(result)
        [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]]
    """

    # Checks if matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) \
       or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(isinstance(num, (int, float)) for
               row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if matrix is None or matrix == []:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Checks if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Checks if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Checks if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divides each element of the matrix by div and round to 2 decimal places
    new_matx = [[round(num / div, 2) for num in row] for row in matrix]

    return new_matx
