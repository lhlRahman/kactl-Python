"""
Author: chilli
License: CC0
Description: z[i] computes the length of the longest common prefix of s[i:] and s,
except z[0] = 0. (abacaba -> 0010301)
Time: O(n)
Status: stress-tested
"""

from typing import List

def Z(S: str) -> List[int]:
    """Compute Z-function for string S"""
    z = [0] * len(S)
    l = -1
    r = -1
    for i in range(1, len(S)):
        z[i] = 0 if i >= r else min(r - i, z[i - l])
        while i + z[i] < len(S) and S[i + z[i]] == S[z[i]]:
            z[i] += 1
        if i + z[i] > r:
            l = i
            r = i + z[i]
    return z

