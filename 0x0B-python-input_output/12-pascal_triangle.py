#!/usr/bin/python3
"""Defines a Pascal's Triangle function.

Defines a function pascal_triangle that generates Pascal's
Triangle of size n. Pascal's Triangle is a triangular array
of binomial coefficients, where each number is the sum of
the two numbers directly above it.

The function takes an integer n as input and returns a list
of lists representing Pascal's Triangle. Each inner list corresponds
to a row in the triangle, and each element in the inner list
represents a number in that row.

This code will generate Pascal's Triangle of size 5 and print
each row of the triangle.

The function starts by checking if n is less than or equal to 0.
If so, it returns an empty list, indicating an invalid input
for the triangle size.

Otherwise, the function initializes the triangles list with the
first row of Pascal's Triangle, which is [1]. It then enters a
loop that continues until the length of triangles is equal to n.

In each iteration of the loop, the function retrieves the last
row of the triangle (tri) and creates a new list "row" with the
first element set to 1. It then iterates over the elements in tri,
except the last one, and appends the sum of each pair of adjacent
elements to "row". Finally, it appends 1 to "row" to complete the
row and adds "row" to the triangles list.

Once the loop finishes, the function returns the generated
Pascal's Triangle as a list of lists.

"""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        row = [1]
        for i in range(len(tri) - 1):
            row.append(tri[i] + tri[i + 1])
        row.append(1)
        triangles.append(row)
    return triangles
