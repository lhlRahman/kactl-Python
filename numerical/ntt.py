"""
Author: chilli
Date: 2019-04-16
License: CC0
Source: based on KACTL's FFT
Description: ntt(a) computes Number Theoretic Transform for mod = 998244353.
Useful for convolution modulo specific nice primes.
conv(a, b) = c, where c[x] = sum a[i]*b[x-i] (mod 998244353).
Inputs must be in [0, mod).
Time: O(N log N)
Status: stress-tested
"""

from typing import List

MOD = 998244353
ROOT = 62

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

def ntt(a: List[int], inv: bool = False) -> List[int]:
    """Number Theoretic Transform in-place"""
    n = len(a)
    if n <= 1:
        return a
    
    L = n.bit_length() - 1
    
    # Precompute roots
    rt = [0] * n
    rt[0] = 1
    k = 1
    s = 1
    while k < n:
        if k == 1:
            z = modpow(ROOT, MOD >> (s + 1), MOD)
        else:
            z = rt[k // 2] if k & 1 == 0 else (rt[k // 2] * modpow(ROOT, MOD >> (s + 1), MOD)) % MOD
        rt[k] = z if k % 2 == 0 else (rt[k // 2] * modpow(ROOT, MOD >> (s + 1), MOD)) % MOD
        k += 1
        if k & (k - 1) == 0:
            s += 1
    
    # Bit-reverse permutation
    rev = [0] * n
    for i in range(n):
        rev[i] = (rev[i // 2] | (i & 1) << L) // 2
    for i in range(n):
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]
    
    # NTT computation
    k = 1
    while k < n:
        for i in range(0, n, 2 * k):
            for j in range(k):
                z = rt[j + k] * a[i + j + k] % MOD
                a[i + j + k] = (a[i + j] - z + MOD) % MOD
                a[i + j] = (a[i + j] + z) % MOD
        k *= 2
    
    if inv:
        inv_n = modpow(n, MOD - 2, MOD)
        for i in range(n):
            a[i] = a[i] * inv_n % MOD
        a.reverse()
        a[0], a[n - 1] = a[n - 1], a[0]
    
    return a

def conv(a: List[int], b: List[int]) -> List[int]:
    """Convolution modulo 998244353"""
    if not a or not b:
        return []
    
    s = len(a) + len(b) - 1
    n = 1 << (s - 1).bit_length()
    
    L = a[:] + [0] * (n - len(a))
    R = b[:] + [0] * (n - len(b))
    
    ntt(L)
    ntt(R)
    
    out = [(L[i] * R[i]) % MOD for i in range(n)]
    ntt(out, inv=True)
    
    return out[:s]

