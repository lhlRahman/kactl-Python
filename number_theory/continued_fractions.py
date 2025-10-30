"""
Author: Simon Lindholm
Date: 2018-07-15
License: CC0
Source: Wikipedia
Description: Given N and a real number x >= 0, finds the closest rational approximation p/q with p, q <= N.
It will obey |p/q - x| <= 1/(qN).
Time: O(log N)
Status: stress-tested for n <= 300
"""

from typing import Tuple

def approximate(x: float, N: int) -> Tuple[int, int]:
    """
    Find closest rational approximation p/q to x with p, q <= N.
    Returns (p, q)
    """
    LP = 0
    LQ = 1
    P = 1
    Q = 0
    inf = 10**18
    y = x
    
    while True:
        lim = min(inf if P == 0 else (N - LP) // P, 
                  inf if Q == 0 else (N - LQ) // Q)
        a = int(y)
        b = min(a, lim)
        NP = b * P + LP
        NQ = b * Q + LQ
        
        if a > b:
            # Semi-convergent case
            return (NP, NQ) if abs(x - NP / NQ) < abs(x - P / Q) else (P, Q)
        
        if abs(y) < 1e-15 or 1 / (y - a) > 3 * N:
            return (NP, NQ)
        
        y = 1 / (y - a)
        LP = P
        P = NP
        LQ = Q
        Q = NQ

