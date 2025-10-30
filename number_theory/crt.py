"""
Author: Simon Lindholm
Date: 2019-05-22
License: CC0
Description: Chinese Remainder Theorem.

crt(a, m, b, n) computes x such that x ≡ a (mod m), x ≡ b (mod n).
If |a| < m and |b| < n, x will obey 0 <= x < lcm(m, n).
Assumes mn < 2^62.
Time: log(n)
Status: Works
"""

from .euclid import euclid

def crt(a: int, m: int, b: int, n: int) -> int:
    """Chinese Remainder Theorem"""
    if n > m:
        a, b = b, a
        m, n = n, m
    
    g, x, y = euclid(m, n)
    assert (a - b) % g == 0, "No solution exists"
    
    x = (b - a) % n * x % n // g * m + a
    return x if x >= 0 else x + m * n // g

