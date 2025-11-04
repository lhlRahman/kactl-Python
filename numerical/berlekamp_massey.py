"""
Author: Lucian Bicsi
Date: 2017-10-31
License: CC0
Source: Wikipedia
Description: Recovers any n-order linear recurrence relation from the first
2n terms of the recurrence.
Useful for guessing linear recurrences after brute-forcing the first terms.
Should work on any field, but numerical stability for floats is not guaranteed.
Output will have size <= n.
Usage: berlekamp_massey([0, 1, 1, 3, 5, 11], mod=1000000007) # [1, 2]
Time: O(N^2)
Status: bruteforce-tested mod 5 for n <= 5 and all s
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

def berlekamp_massey(s: List[int], mod: int = 10**9 + 7) -> List[int]:
    """
    Find minimal linear recurrence for sequence s.
    Returns coefficients [c1, c2, ...] where s[i] = c1*s[i-1] + c2*s[i-2] + ...
    """
    n = len(s)
    L = 0
    m = 0
    C = [0] * n
    B = [0] * n
    C[0] = B[0] = 1
    
    b = 1
    for i in range(n):
        m += 1
        d = s[i] % mod
        for j in range(1, L + 1):
            d = (d + C[j] * s[i - j]) % mod
        if d == 0:
            continue
        T = C[:]
        coef = d * modpow(b, mod - 2, mod) % mod
        for j in range(m, n):
            C[j] = (C[j] - coef * B[j - m]) % mod
        if 2 * L > i:
            continue
        L = i + 1 - L
        B = T
        b = d
        m = 0
    
    C = C[:L + 1]
    C = C[1:]
    for i in range(len(C)):
        C[i] = (mod - C[i]) % mod
    return C

