"""
Author: Unknown
Date: 2002-09-15
Source: predates tinyKACTL
Description: Finds two integers x and y, such that ax+by=gcd(a,b).
If you just need gcd, use math.gcd instead.
If a and b are coprime, then x is the inverse of a (mod b).
"""

from typing import Tuple

def euclid(a: int, b: int) -> Tuple[int, int, int]:
    """
    Extended Euclidean Algorithm.
    Returns (gcd, x, y) where ax + by = gcd(a, b)
    """
    if b == 0:
        return (a, 1, 0)
    
    d, y, x = euclid(b, a % b)
    y -= (a // b) * x
    return (d, x, y)
