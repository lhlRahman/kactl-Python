"""
Author: Lucian Bicsi
Date: 2015-06-25
License: GNU Free Documentation License 1.2
Source: csacademy
Description: Transform to a basis with fast convolutions of the form
c[z] = sum_{z = x op y} a[x] * b[y],
where op is one of AND, OR, XOR. The size of a must be a power of two.
Time: O(N log N)
Status: stress-tested
"""

from typing import List

def fst_and(a: List[int], inv: bool = False) -> List[int]:
    """Fast Subset Transform for AND operation"""
    n = len(a)
    a = a[:]
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                if inv:
                    a[j], a[j + step] = v - u, u
                else:
                    a[j], a[j + step] = v, u + v
        step *= 2
    return a

def fst_or(a: List[int], inv: bool = False) -> List[int]:
    """Fast Subset Transform for OR operation"""
    n = len(a)
    a = a[:]
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                if inv:
                    a[j], a[j + step] = v, u - v
                else:
                    a[j], a[j + step] = u + v, u
        step *= 2
    return a

def fst_xor(a: List[int], inv: bool = False) -> List[int]:
    """Fast Subset Transform for XOR operation"""
    n = len(a)
    a = a[:]
    step = 1
    while step < n:
        for i in range(0, n, 2 * step):
            for j in range(i, i + step):
                u, v = a[j], a[j + step]
                a[j], a[j + step] = u + v, u - v
        step *= 2
    if inv:
        for i in range(n):
            a[i] //= n
    return a

def conv_and(a: List[int], b: List[int]) -> List[int]:
    """Convolution using AND"""
    a = fst_and(a)
    b = fst_and(b)
    c = [a[i] * b[i] for i in range(len(a))]
    return fst_and(c, inv=True)

def conv_or(a: List[int], b: List[int]) -> List[int]:
    """Convolution using OR"""
    a = fst_or(a)
    b = fst_or(b)
    c = [a[i] * b[i] for i in range(len(a))]
    return fst_or(c, inv=True)

def conv_xor(a: List[int], b: List[int]) -> List[int]:
    """Convolution using XOR"""
    a = fst_xor(a)
    b = fst_xor(b)
    c = [a[i] * b[i] for i in range(len(a))]
    return fst_xor(c, inv=True)

