"""
Author: Simon Lindholm
Date: 2019-12-28
License: CC0
Source: https://github.com/hoke-t/tamu-kactl/blob/master/content/data-structures/MoQueries.h
Description: Answer interval or tree path queries by finding an approximate TSP through the queries,
and moving from one query to the next by adding/removing points at the ends.
Time: O(N √Q)
Status: stress-tested
"""

from typing import List, Tuple, Callable

def mo_queries(Q: List[Tuple[int, int]], 
               add: Callable[[int, int], None],
               delete: Callable[[int, int], None],
               calc: Callable[[], int],
               blk: int = 350) -> List[int]:
    """
    Answer interval queries using Mo's algorithm.
    Q = list of (left, right) queries
    add(ind, end) = function to add a[ind] (end = 0 for left, 1 for right)
    delete(ind, end) = function to remove a[ind]
    calc() = function to compute current answer
    blk = block size (~N/√Q)
    Returns list of answers for each query
    """
    L = 0
    R = 0
    s = list(range(len(Q)))
    res = [0] * len(Q)
    
    # Sort queries by (block, right endpoint with alternating order)
    def sort_key(i):
        block = Q[i][0] // blk
        r = Q[i][1]
        if block & 1:
            r = -r
        return (block, r)
    
    s.sort(key=sort_key)
    
    for qi in s:
        q = Q[qi]
        # Expand/contract the window
        while L > q[0]:
            L -= 1
            add(L, 0)
        while R < q[1]:
            add(R, 1)
            R += 1
        while L < q[0]:
            delete(L, 0)
            L += 1
        while R > q[1]:
            R -= 1
            delete(R, 1)
        res[qi] = calc()
    
    return res

