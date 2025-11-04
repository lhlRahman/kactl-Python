"""
Author: Simon Lindholm
Date: 2016-12-08
Source: The regular matrix inverse code
Description: Invert matrix A modulo a prime.
Returns rank; result is stored in A unless singular (rank < n).
Time: O(n^3)
Status: Slightly tested
"""

from typing import List

def modpow(base: int, exp: int, mod: int) -> int:
    """Modular exponentiation"""
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

def matrix_inverse_mod(A: List[List[int]], mod: int) -> int:
    """
    Compute matrix inverse modulo a prime.
    A = matrix to invert (modified in-place to contain inverse)
    mod = prime modulus
    Returns rank (n if successful, < n if singular)
    """
    n = len(A)
    col = list(range(n))
    tmp = [[0] * n for _ in range(n)]
    
    # Initialize tmp as identity
    for i in range(n):
        tmp[i][i] = 1
    
    # Forward elimination
    for i in range(n):
        # Find pivot
        r = i
        c = i
        found = False
        for j in range(i, n):
            for k in range(i, n):
                if A[j][k] != 0:
                    r = j
                    c = k
                    found = True
                    break
            if found:
                break
        
        if not found:
            return i  # Singular matrix
        
        # Swap rows
        A[i], A[r] = A[r], A[i]
        tmp[i], tmp[r] = tmp[r], tmp[i]
        
        # Swap columns
        for j in range(n):
            A[j][i], A[j][c] = A[j][c], A[j][i]
            tmp[j][i], tmp[j][c] = tmp[j][c], tmp[j][i]
        col[i], col[c] = col[c], col[i]
        
        # Eliminate
        v = modpow(A[i][i], mod - 2, mod)
        for j in range(i + 1, n):
            f = A[j][i] * v % mod
            A[j][i] = 0
            for k in range(i + 1, n):
                A[j][k] = (A[j][k] - f * A[i][k]) % mod
            for k in range(n):
                tmp[j][k] = (tmp[j][k] - f * tmp[i][k]) % mod
        
        # Normalize pivot row
        for j in range(i + 1, n):
            A[i][j] = A[i][j] * v % mod
        for j in range(n):
            tmp[i][j] = tmp[i][j] * v % mod
        A[i][i] = 1
    
    # Backward elimination
    for i in range(n - 1, 0, -1):
        for j in range(i):
            v = A[j][i]
            for k in range(n):
                tmp[j][k] = (tmp[j][k] - v * tmp[i][k]) % mod
    
    # Restore column order and ensure positive values
    for i in range(n):
        for j in range(n):
            val = tmp[i][j] % mod
            A[col[i]][col[j]] = val if val >= 0 else val + mod
    
    return n

