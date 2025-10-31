"""
Author: someone on Codeforces
Date: 2017-03-14
Source: folklore
Description: A short self-balancing tree. It acts as a
sequential container with log-time splits/joins, and
is easy to augment with additional data.
Time: O(log N)
Status: stress-tested
"""

import random
from typing import Optional, Tuple, Callable

class TreapNode:
    def __init__(self, val: int):
        self.l: Optional['TreapNode'] = None
        self.r: Optional['TreapNode'] = None
        self.val = val
        self.y = random.randint(0, 2**31 - 1)
        self.c = 1  # count of nodes in subtree
    
    def recalc(self):
        """Recalculate subtree size"""
        self.c = cnt(self.l) + cnt(self.r) + 1

def cnt(n: Optional[TreapNode]) -> int:
    """Get count of nodes in subtree"""
    return n.c if n else 0

def each(n: Optional[TreapNode], f: Callable[[int], None]):
    """Apply function f to each value in-order"""
    if n:
        each(n.l, f)
        f(n.val)
        each(n.r, f)

def split(n: Optional[TreapNode], k: int) -> Tuple[Optional[TreapNode], Optional[TreapNode]]:
    """Split treap at position k"""
    if not n:
        return None, None
    
    if cnt(n.l) >= k:  # For lower_bound(k), use "n.val >= k"
        L, R = split(n.l, k)
        n.l = R
        n.recalc()
        return L, n
    else:
        L, R = split(n.r, k - cnt(n.l) - 1)  # For lower_bound, use just "k"
        n.r = L
        n.recalc()
        return n, R

def merge(l: Optional[TreapNode], r: Optional[TreapNode]) -> Optional[TreapNode]:
    """Merge two treaps"""
    if not l:
        return r
    if not r:
        return l
    
    if l.y > r.y:
        l.r = merge(l.r, r)
        l.recalc()
        return l
    else:
        r.l = merge(l, r.l)
        r.recalc()
        return r

def insert(t: Optional[TreapNode], n: TreapNode, pos: int) -> TreapNode:
    """Insert node n at position pos"""
    l, r = split(t, pos)
    return merge(merge(l, n), r)

def move(t: TreapNode, l: int, r: int, k: int) -> TreapNode:
    """Move range [l, r) to index k"""
    a, b = split(t, l)
    b, c = split(b, r - l)
    if k <= l:
        return merge(insert(a, b, k), c)
    else:
        return merge(a, insert(c, b, k - r))

