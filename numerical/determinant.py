"""
Author: Simon Lindholm
Date: 2016-09-06
License: CC0
Source: folklore
Description: Calculates determinant of a matrix. Destroys the matrix.
Time: O(N^3)
Status: somewhat tested
"""

from typing import List

def determinant(a: List[List[float]]) -> float:
    """
    Calculate determinant of matrix a.
    Warning: modifies input matrix
    """
    n = len(a)
    res = 1.0
    
    for i in range(n):
        # Find pivot
        b = i
        for j in range(i + 1, n):
            if abs(a[j][i]) > abs(a[b][i]):
                b = j
        
        if i != b:
            a[i], a[b] = a[b], a[i]
            res *= -1
        
        res *= a[i][i]
        if res == 0:
            return 0
        
        # Eliminate column
        for j in range(i + 1, n):
            v = a[j][i] / a[i][i]
            if v != 0:
                for k in range(i + 1, n):
                    a[j][k] -= v * a[i][k]
    
    return res

