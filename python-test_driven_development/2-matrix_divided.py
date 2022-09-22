#!/usr/bin/python3
"""
function matrix divided
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix

    Args:
        matrix: The list of the list
        divide: number which divide in matrix

    Return:
        a new matrix after divide
    """
    if isinstance(matrix, list) is False:
        raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")

    for elems in matrix:
        if isinstance(elems, list) is False:
            raise TypeError("matrix must be a matrix (list of lists) of \
integers/floats")
    if isinstance(div, (int, float)) is False:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        new = []
        size = len(matrix[0])
        for i in range(len(matrix)):
            if len(matrix[i]) != size:
                raise TypeError("Each row of the matrix must have \
the same size")
            new.append([])
            for j in range(len(matrix[i])):
                if isinstance(matrix[i][j], (int, float)) is False:
                    raise TypeError("matrix must be a matrix (list of lists) \
of integers/floats")
                new[i].append(round(matrix[i][j] / div, 2))
        return new
