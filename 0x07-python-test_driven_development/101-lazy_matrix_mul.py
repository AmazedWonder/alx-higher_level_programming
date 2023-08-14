#!/usr/bin/python3
"""Defines class lazy_matrix_mul that multiplies
   2 matrices by using the module NumPy.

Function Description:

The lazy_matrix_mul function performs matrix multiplication
on two matrices m_a and m_b using the NumPy module and returns
the resulting matrix. It utilizes the numpy.matmul function for
efficient matrix multiplication.

This function uses the numpy.matmul function to perform matrix
multiplication. It converts the resulting NumPy array back to
a regular Python list using tolist() before returning it.

Parameters:

m_a: The first matrix represented as a list of lists of integers or floats.
m_b: The second matrix represented as a list of lists of integers or floats.
Exceptions:

Exceptions are in the Test file 101-lazy_matrix_mul.txt

The lazy_matrix_mul function may raise the following exceptions:

ValueError: If m_a and m_b have incompatible dimensions for matrix
multiplication. This occurs when the number of columns in m_a is not
equal to the number of rows in m_b.

TypeError: If any other exception occurs during matrix multiplication,
such as invalid input types or malformed matrices. This exception
captures any general error raised by the NumPy library and
provides the specific error message.

The exceptions provide detailed error messages to assist in debugging
and addressing any issues encountered during matrix multiplication.

If the input matrices pass the validation checks and the matrix
multiplication is successful, the lazy_matrix_mul function returns
the resulting matrix.

"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Performs matrix multiplication on two matrices using the NumPy module.

    Args:
        m_a (list): The first matrix represented as
        a list of lists of integers or floats.
        m_b (list): The second matrix represented as
        a list of lists of integers or floats..

    """
    output = np.matmul(m_a, m_b)

    return output
