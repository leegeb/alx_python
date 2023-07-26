#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result_matrix = []
    for row in matrix:
        result_row = []
        for element in row:
            squared_value = element ** 2
            result_row.append(squared_value)
        result_matrix.append(result_row)
    return result_matrix