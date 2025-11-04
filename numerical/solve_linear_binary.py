"""
Author: Simon Lindholm
Date: 2016-08-27
License: CC0
Source: own work
Description: Solves Ax = b over F_2 (binary field).
If there are multiple solutions, one is returned arbitrarily.
Returns rank, or -1 if no solutions.
Time: O(n^2 m)
Status: bruteforce-tested for n, m <= 4
"""

from typing import List

def solve_linear_binary(A: List[List[int]], b: List[int], m: int) -> tuple:
    """
    Solve linear system over F_2 (binary field).
    A = coefficient matrix (modified)
    b = RHS vector (modified)
    m = number of variables
    Returns (rank, solution) or (-1, None) if no solution
    solution is a list of length m with 0/1 values
    """
    n = len(A)
    rank = 0
    col = list(range(m))
    
    for i in range(n):
        # Find pivot
        br = -1
        for row in range(i, n):
            if any(A[row]):
                br = row
                break
        
        if br == -1:
            # Check if remaining equations are consistent
            for j in range(i, n):
                if b[j]:
                    return (-1, None)
            break
        
        # Find first nonzero column
        bc = -1
        for c in range(i, m):
            if A[br][c]:
                bc = c
                break
        
        # Swap rows and columns
        A[i], A[br] = A[br], A[i]
        b[i], b[br] = b[br], b[i]
        col[i], col[bc] = col[bc], col[i]
        
        for j in range(n):
            if A[j][i] != A[j][bc]:
                A[j][i] ^= 1
                A[j][bc] ^= 1
        
        # Eliminate
        for j in range(i + 1, n):
            if A[j][i]:
                b[j] ^= b[i]
                for k in range(m):
                    A[j][k] ^= A[i][k]
        
        rank += 1
    
    # Back substitution
    x = [0] * m
    for i in range(rank - 1, -1, -1):
        if b[i]:
            x[col[i]] = 1
            for j in range(i):
                b[j] ^= A[j][i]
    
    return (rank, x)

