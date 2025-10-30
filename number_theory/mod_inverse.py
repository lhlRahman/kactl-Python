"""
Author: Simon Lindholm
Date: 2016-07-24
License: CC0
Source: Russian page
Description: Pre-computation of modular inverses. Assumes LIM <= mod and that mod is a prime.
Status: Works
"""

from typing import List

def compute_inverses(LIM: int, mod: int) -> List[int]:
    """Pre-compute modular inverses for 1 to LIM-1 modulo mod (mod must be prime)"""
    inv = [0] * LIM
    inv[1] = 1
    for i in range(2, LIM):
        inv[i] = mod - (mod // i) * inv[mod % i] % mod
    return inv

