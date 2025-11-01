"""
Author: Unknown
Date: 2002-09-13
Source: predates tinyKACTL
Description: Topological sorting. Given is an oriented graph.
Output is an ordering of vertices, such that there are edges only from left to right.
If there are cycles, the returned list will have size smaller than n -- nodes reachable
from cycles will not be returned.
Time: O(|V|+|E|)
Status: stress-tested
"""

from typing import List

def topo_sort(gr: List[List[int]]) -> List[int]:
    """
    Topological sort using Kahn's algorithm.
    gr[i] = list of neighbors of node i
    Returns topologically sorted list (empty or partial if cycle exists)
    """
    indeg = [0] * len(gr)
    
    # Calculate in-degrees
    for neighbors in gr:
        for x in neighbors:
            indeg[x] += 1
    
    # Start with nodes having in-degree 0
    q = [i for i in range(len(gr)) if indeg[i] == 0]
    
    # Process queue
    j = 0
    while j < len(q):
        for x in gr[q[j]]:
            indeg[x] -= 1
            if indeg[x] == 0:
                q.append(x)
        j += 1
    
    return q
