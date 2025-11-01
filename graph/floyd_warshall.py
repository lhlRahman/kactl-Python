"""
Author: Simon Lindholm
Date: 2016-12-15
License: CC0
Source: http://en.wikipedia.org/wiki/Floyd–Warshall_algorithm
Description: Calculates all-pairs shortest path in a directed graph that might have negative edge weights.
Input is a distance matrix m, where m[i][j] = inf if i and j are not adjacent.
As output, m[i][j] is set to the shortest distance between i and j, inf if no path,
or -inf if the path goes through a negative-weight cycle.
Time: O(N^3)
Status: slightly tested
"""

from typing import List

INF = 10**18

def floyd_warshall(m: List[List[int]]):
    """
    All-pairs shortest path with negative weights.
    m = adjacency matrix (modified in-place)
    m[i][j] = weight of edge i->j, or INF if no edge
    After: m[i][j] = shortest path distance, INF if unreachable, -INF if negative cycle
    """
    n = len(m)
    
    # Initialize diagonal
    for i in range(n):
        m[i][i] = min(m[i][i], 0)
    
    # Floyd-Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if m[i][k] != INF and m[k][j] != INF:
                    new_dist = max(m[i][k] + m[k][j], -INF)
                    m[i][j] = min(m[i][j], new_dist)
    
    # Detect and propagate negative cycles
    for k in range(n):
        if m[k][k] < 0:
            for i in range(n):
                for j in range(n):
                    if m[i][k] != INF and m[k][j] != INF:
                        m[i][j] = -INF
