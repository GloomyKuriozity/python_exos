"""
PROGRAM NAME - transpose_matrix
PROGRAMMER - Kuriozity
LANGUAGE - Python + numpy
SYSTEM - Windows 11
DATE - Completed 21/06/2023
NDP - None :)
"""

import numpy as np

def transpose_matrix(matrix):
    """
    Transpose a matrix.
    
    Args:
        matrix (square list): matrix to transpose.
    
    Returns:
        transposed matrix (square list): matrix transposed.
    """
    
    return np.transpose(matrix)
    

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose_matrix(matrix))
