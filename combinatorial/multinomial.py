"""
Author: Mattias de Zalenski, Fredrik Niemelä, Per Austrin, Simon Lindholm
Date: 2002-09-26
Source: Max Bennedich
Description: Computes multinomial coefficient (k1 + ... + kn)! / (k1! * k2! * ... * kn!)
Status: Tested on kattis:lexicography
"""

from typing import List

def multinomial(v: List[int]) -> int:
    """
    Compute multinomial coefficient.
    v = list of partition sizes
    Returns (sum v_i)! / (v_1! * v_2! * ... * v_n!)
    """
    if not v:
        return 1
    
    c = 1
    m = v[0]
    for i in range(1, len(v)):
        for j in range(v[i]):
            m += 1
            c = c * m // (j + 1)
    return c

