"""
Author: Simon Lindholm
Date: 2018-07-06
License: CC0
Description: Permutation -> integer conversion. (Not order preserving.)
Integer -> permutation can use a lookup table.
Time: O(n)
"""

from typing import List

def perm_to_int(v: List[int]) -> int:
    """Convert permutation to integer"""
    use = 0
    i = 0
    r = 0
    for x in v:
        i += 1
        # Count how many bits are set in use for positions < x
        r = r * i + bin(use & -(1 << x)).count('1')
        use |= 1 << x
    return r

