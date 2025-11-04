"""
Author: Ulf Lundstrom, Simon Lindholm
Date: 2009-08-15
License: CC0
Source: https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
Description: x = tridiagonal(d, p, q, b) solves a tridiagonal system.
Useful for solving problems of the form a_i = b_i * a_{i-1} + c_i * a_{i+1} + d_i.
Fails if the solution is not unique.
If |d_i| > |p_i| + |q_{i-1}| for all i, or |d_i| > |p_{i-1}| + |q_i|, 
or the matrix is positive definite, the algorithm is numerically stable.
Time: O(N)
Status: Brute-force tested mod 5 and 7 and stress-tested for real matrices
"""

from typing import List

def tridiagonal(diag: List[float], super_diag: List[float], 
                sub_diag: List[float], b: List[float]) -> List[float]:
    """
    Solve tridiagonal system.
    diag = main diagonal
    super_diag = super diagonal (above main)
    sub_diag = sub diagonal (below main)
    b = right hand side
    Returns solution vector
    """
    n = len(b)
    tr = [0] * n
    diag = diag[:]  # Copy to avoid modifying input
    b = b[:]
    
    for i in range(n - 1):
        if abs(diag[i]) < 1e-9 * abs(super_diag[i]):  # diag[i] == 0
            b[i + 1] -= b[i] * diag[i + 1] / super_diag[i]
            if i + 2 < n:
                b[i + 2] -= b[i] * sub_diag[i + 1] / super_diag[i]
            diag[i + 1] = sub_diag[i]
            i += 1
            tr[i] = 1
        else:
            diag[i + 1] -= super_diag[i] * sub_diag[i] / diag[i]
            b[i + 1] -= b[i] * sub_diag[i] / diag[i]
    
    for i in range(n - 1, -1, -1):
        if tr[i]:
            b[i], b[i - 1] = b[i - 1], b[i]
            diag[i - 1] = diag[i]
            b[i] /= super_diag[i - 1]
        else:
            b[i] /= diag[i]
            if i:
                b[i - 1] -= b[i] * super_diag[i - 1]
    
    return b

