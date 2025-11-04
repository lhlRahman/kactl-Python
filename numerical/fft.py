"""
Author: Ludo Pulles, chilli, Simon Lindholm
Date: 2019-01-09
License: CC0
Source: http://neerc.ifmo.ru/trains/toulouse/2017/fft2.pdf
Description: fft(a) computes FFT. Useful for convolution.
conv(a, b) = c, where c[x] = sum a[i]*b[x-i].
Rounding is safe if (sum a_i^2 + sum b_i^2)*log2(N) < 9*10^14.
Time: O(N log N) with N = |A|+|B|
Status: somewhat tested
"""

import cmath
from typing import List

def fft(a: List[complex], inv: bool = False) -> List[complex]:
    """FFT in-place"""
    n = len(a)
    if n <= 1:
        return a
    
    L = n.bit_length() - 1
    
    # Bit-reverse permutation
    rev = [0] * n
    for i in range(n):
        rev[i] = (rev[i // 2] | (i & 1) << L) // 2
    for i in range(n):
        if i < rev[i]:
            a[i], a[rev[i]] = a[rev[i]], a[i]
    
    # FFT computation
    k = 1
    while k < n:
        angle = (-2 if inv else 2) * cmath.pi / (2 * k)
        w_len = complex(cmath.cos(angle), cmath.sin(angle))
        for i in range(0, n, 2 * k):
            w = complex(1, 0)
            for j in range(k):
                u = a[i + j]
                v = a[i + j + k] * w
                a[i + j] = u + v
                a[i + j + k] = u - v
                w *= w_len
        k *= 2
    
    if inv:
        for i in range(n):
            a[i] /= n
    
    return a

def conv(a: List[float], b: List[float]) -> List[float]:
    """Convolution of two arrays"""
    if not a or not b:
        return []
    
    res_len = len(a) + len(b) - 1
    n = 1 << (res_len - 1).bit_length()
    
    # Prepare input
    fa = [complex(a[i] if i < len(a) else 0, b[i] if i < len(b) else 0) for i in range(n)]
    
    fft(fa)
    
    # Multiply
    for i in range(n):
        fa[i] = fa[i] * fa[i]
    
    # Prepare output
    out = [complex(0, 0)] * n
    for i in range(n):
        j = (-i) & (n - 1)
        out[i] = fa[j] - fa[i].conjugate()
    
    fft(out, inv=True)
    
    return [out[i].imag / 4 for i in range(res_len)]

