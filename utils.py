"""
Common utilities and helper functions for Python KACTL algorithms.
Equivalents of the C++ macros and typedefs used in the original code.
"""
import math
import random
from typing import List, Tuple, Any

# Type aliases (equivalents of C++ typedefs)
vi = List[int]
vll = List[int]
pii = Tuple[int, int]
pll = Tuple[int, int]

def rep(start: int, end: int):
    """Equivalent of rep(i, a, b) macro"""
    return range(start, end)

def sz(container) -> int:
    """Equivalent of sz(x) macro"""
    return len(container)

def bit_floor(n: int) -> int:
    """Find the largest power of 2 <= n"""
    if n == 0:
        return 0
    return 1 << (n.bit_length() - 1)

def bit_ceil(n: int) -> int:
    """Find the smallest power of 2 >= n"""
    if n == 0:
        return 1
    if n & (n - 1) == 0:
        return n
    return 1 << n.bit_length()

def clz(n: int) -> int:
    """Count leading zeros (equivalent to __builtin_clz for 32-bit)"""
    if n == 0:
        return 32
    return 31 - n.bit_length() + 1

def popcount(n: int) -> int:
    """Count number of set bits"""
    return bin(n).count('1')

