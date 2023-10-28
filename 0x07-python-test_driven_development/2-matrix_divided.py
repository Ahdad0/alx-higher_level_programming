#!/usr/bin/python3

"""
    function matrix_divided divide matrix by div and return
    a new matrix and if raise exceptions if they excpect any
"""


def matrix_divided(matrix, div):
    """
        return a new matrix divided by div
    """
    new_list = [[i for i in range(len(matrix[0]))] for k in range(len(matrix))]
    error = 0
    message = '(list of lists) of integers/floats'

    if div == 0:
        raise ZeroDivisionError('division by zero')
    elif not (type(div) is int or type(div) is float):
        raise TypeError('div must be a number')

    for index, value in enumerate(matrix):
        if len(matrix) != index + 1:
            if len(matrix[index]) != len(matrix[index + 1]):
                error = 1
                break

        for row, row_value in enumerate(value):
            if not (type(row_value) is int or type(row_value) is float):
                error = 2
                break

            result = '{:.2f}'.format(row_value / div)
            new_list[index][row] = float(result)

    if error == 1:
        raise TypeError('Each row of the matrix must have the same size')
    elif error == 2:
        raise TypeError('matrix must be a matrix ' +  message)

    return new_list
