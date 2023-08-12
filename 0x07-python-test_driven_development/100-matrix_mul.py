#!/usr/bin/python3
"""Defines function that performs matrix multiplication
   on two matrices m_a and m_b.

Function Description:

The matrix_mul function performs matrix multiplication on two
matrices m_a and m_b and returns the resulting matrix. It
follows a set of validation requirements to ensure that the
input matrices meet the necessary criteria for multiplication.

Parameters:

m_a: The first matrix represented as a
list of lists of integers or floats.
m_b: The second matrix represented as a
list of lists of integers or floats.
Exceptions:

The matrix_mul function raise the following exceptions:

TypeError: If m_a or m_b is not a list, or if
any element within the matrices is not an integer or a float, or
if the rows within m_a or m_b are not of the same size.
ValueError: If m_a or m_b is an empty list or a
list containing an empty list.
ValueError: If the dimensions of m_a and m_b are incompatible for
matrix multiplication.

"""


def matrix_mul(m_a, m_b):
    """ Function multiplies 2 matrices

    Args:
        m_a: matrix a
        m_b: matrix b

    Returns:
        result of the multipliction.

    Raises:
        TypeError: If m_a or m_b is not a list
        TypeError: if any element within the matrices
                   is not an integer or a float
        TypeError: if the rows within m_a or m_b are not of the same size
        ValueError: If m_a or m_b is an empty list or a list
                    containing an empty list.
        ValueError: If the dimensions of m_a and m_b are incompatible
                    for matrix multiplication.

    """
    # Validate m_a and m_b
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    if not all(isinstance(element, (int, float))
               for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(element, (int, float))
               for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    if any(len(row) != len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    output = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_a[0])):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        output.append(row)

    return output
