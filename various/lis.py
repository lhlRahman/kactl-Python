"""
Author: Johan Sannemo
License: CC0
Description: Compute indices for the longest increasing subsequence.
Time: O(N log N)
Status: Tested on kattis:longincsubseq, stress-tested
"""

from typing import List, TypeVar
import bisect

T = TypeVar('T')

def lis(S: List[T]) -> List[int]:
    """
    Find longest increasing subsequence.
    Returns list of indices in S forming the LIS.
    For longest non-decreasing, use bisect_right instead of bisect_left.
    """
    if not S:
        return []
    
    prev = [0] * len(S)
    res = []  # list of (value, index) pairs
    
    for i in range(len(S)):
        # For longest non-decreasing, change bisect_left to bisect_right
        pos = bisect.bisect_left(res, (S[i], 0))
        
        if pos == len(res):
            res.append((S[i], i))
        else:
            res[pos] = (S[i], i)
        
        prev[i] = 0 if pos == 0 else res[pos - 1][1]
    
    L = len(res)
    cur = res[-1][1]
    ans = [0] * L
    while L > 0:
        L -= 1
        ans[L] = cur
        cur = prev[cur]
    
    return ans
