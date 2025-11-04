"""
Author: Simon Lindholm
License: CC0
Source: Codeforces
Description: Given a[i] = min_{lo(i) <= k < hi(i)}(f(i, k)) where the (minimal)
optimal k increases with i, computes a[i] for i = L..R-1.
Time: O((N + (hi-lo)) log N)
Status: tested on http://codeforces.com/contest/321/problem/E
"""

from typing import Callable, Any, List

class DivideAndConquerDP:
    """
    Divide and Conquer DP optimization.
    Use when optimal k increases monotonically with i.
    """
    
    def __init__(self, 
                 lo_func: Callable[[int], int],
                 hi_func: Callable[[int], int],
                 cost_func: Callable[[int, int], int]):
        """
        lo_func(i) = minimum k to consider for state i
        hi_func(i) = maximum k to consider for state i
        cost_func(i, k) = cost of transition from k to i
        """
        self.lo = lo_func
        self.hi = hi_func
        self.f = cost_func
        self.result = {}
    
    def rec(self, L: int, R: int, LO: int, HI: int):
        """Recursively solve subproblem"""
        if L >= R:
            return
        
        mid = (L + R) >> 1
        best_val = float('inf')
        best_k = LO
        
        for k in range(max(LO, self.lo(mid)), min(HI, self.hi(mid))):
            val = self.f(mid, k)
            if val < best_val:
                best_val = val
                best_k = k
        
        self.result[mid] = (best_k, best_val)
        
        self.rec(L, mid, LO, best_k + 1)
        self.rec(mid + 1, R, best_k, HI)
    
    def solve(self, L: int, R: int) -> dict:
        """
        Solve for range [L, R).
        Returns dict mapping i to (optimal_k, optimal_value)
        """
        self.result = {}
        self.rec(L, R, -(10**9), 10**9)
        return self.result

