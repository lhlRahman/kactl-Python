"""
Author: Mårten Wiman
License: CC0
Source: Pisinger 1999, "Linear Time Algorithms for Knapsack Problems with Bounded Weights"
Description: Given N non-negative integer weights w and a non-negative target t,
computes the maximum S <= t such that S is the sum of some subset of the weights.
Time: O(N * max(w_i))
Status: Tested on kattis:eavesdropperevasion, stress-tested
"""

from typing import List

def fast_knapsack(w: List[int], t: int) -> int:
    """
    Fast subset sum / knapsack solver.
    w = list of weights
    t = target sum
    Returns maximum sum <= t that can be achieved
    """
    a = 0
    b = 0
    
    # Greedy phase
    while b < len(w) and a + w[b] <= t:
        a += w[b]
        b += 1
    
    if b == len(w):
        return a
    
    # DP phase
    m = max(w)
    v = [-1] * (2 * m)
    v[a + m - t] = b
    
    for i in range(b, len(w)):
        u = v[:]
        for x in range(m):
            if v[x + w[i]] < u[x]:
                v[x + w[i]] = u[x]
        
        x = 2 * m - 1
        while x > m:
            if u[x] >= 0:
                for j in range(max(0, u[x]), min(len(w), v[x])):
                    if v[x - w[j]] < j:
                        v[x - w[j]] = j
            x -= 1
    
    # Find maximum achievable sum
    a = t
    while a >= 0 and v[a + m - t] < 0:
        a -= 1
    
    return a

