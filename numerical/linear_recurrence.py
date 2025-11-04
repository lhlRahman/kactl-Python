"""
Author: Lucian Bicsi
Date: 2018-02-14
License: CC0
Source: Chinese material
Description: Generates the k'th term of an n-order
linear recurrence S[i] = sum_j S[i-j-1]*tr[j],
given S[0 ... >= n-1] and tr[0 ... n-1].
Faster than matrix multiplication.
Useful together with Berlekamp-Massey.
Usage: linear_recurrence([0, 1], [1, 1], k, mod) # k'th Fibonacci number
Time: O(n^2 log k)
Status: bruteforce-tested mod 5 for n <= 5
"""

from typing import List

def linear_recurrence(S: List[int], tr: List[int], k: int, mod: int = 10**9 + 7) -> int:
    """
    Compute k'th term of linear recurrence.
    S = initial terms
    tr = transition coefficients
    k = index to compute
    mod = modulus
    """
    n = len(tr)
    
    def combine(a: List[int], b: List[int]) -> List[int]:
        """Combine two polynomials"""
        res = [0] * (n * 2 + 1)
        for i in range(n + 1):
            for j in range(n + 1):
                res[i + j] = (res[i + j] + a[i] * b[j]) % mod
        for i in range(2 * n, n, -1):
            for j in range(n):
                res[i - 1 - j] = (res[i - 1 - j] + res[i] * tr[j]) % mod
        return res[:n + 1]
    
    pol = [0] * (n + 1)
    e = [0] * (n + 1)
    pol[0] = 1
    e[1] = 1
    
    k += 1
    while k:
        if k % 2:
            pol = combine(pol, e)
        e = combine(e, e)
        k //= 2
    
    res = 0
    for i in range(n):
        res = (res + pol[i + 1] * S[i]) % mod
    return res

