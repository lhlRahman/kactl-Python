"""
Author: chilli, Takanori MAEHARA
Date: 2020-04-03
License: CC0
Source: https://github.com/spaghetti-source/algorithm
Description: Given a list of edges representing an undirected flow graph,
returns edges of the Gomory-Hu tree. The max flow between any pair of
vertices is given by minimum edge weight along the Gomory-Hu tree path.
Time: O(V) Flow Computations
Status: Tested on CERC 2015 J, stress-tested

Details: Uses Gusfield's simplified version of Gomory-Hu.
"""

from typing import List, Tuple
from .push_relabel import PushRelabel

def gomory_hu(N: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Construct Gomory-Hu tree.
    N = number of vertices
    edges = list of (u, v, capacity) tuples
    Returns list of tree edges (u, v, flow_value)
    """
    tree = []
    par = [0] * N
    
    for i in range(1, N):
        # Run max flow between i and par[i]
        flow = PushRelabel(N)
        for u, v, cap in edges:
            flow.add_edge(u, v, cap, cap)  # Undirected
        
        flow_value = flow.calc(i, par[i])
        tree.append((i, par[i], flow_value))
        
        # Update parents based on min cut
        for j in range(i + 1, N):
            if par[j] == par[i] and flow.left_of_min_cut(j):
                par[j] = i
    
    return tree

