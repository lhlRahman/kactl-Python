"""
Author: Simon Lindholm
Date: 2021-01-09
License: CC0
Source: https://en.wikipedia.org/wiki/Stoer–Wagner_algorithm
Description: Find a global minimum cut in an undirected graph,
as represented by an adjacency matrix.
Time: O(V^3)
Status: Stress-tested together with GomoryHu
"""

from typing import List, Tuple

def global_min_cut(mat: List[List[int]]) -> Tuple[int, List[int]]:
    """
    Find global minimum cut in undirected graph.
    mat = adjacency matrix (mat[i][j] = weight of edge i-j)
    Returns (cut_weight, nodes_on_one_side)
    """
    n = len(mat)
    mat = [row[:] for row in mat]  # Copy matrix
    
    best_weight = float('inf')
    best_cut = []
    
    # co[i] = list of original nodes merged into node i
    co = [[i] for i in range(n)]
    
    for ph in range(1, n):
        w = mat[0][:]
        s = 0
        t = 0
        
        for it in range(n - ph):
            w[t] = float('-inf')
            s = t
            # Find node with maximum weight
            t = max(range(n), key=lambda i: w[i])
            # Update weights
            for i in range(n):
                w[i] += mat[t][i]
        
        # Check if this is a better cut
        cut_weight = w[t] - mat[t][t]
        if cut_weight < best_weight:
            best_weight = cut_weight
            best_cut = co[t][:]
        
        # Merge t into s
        co[s].extend(co[t])
        for i in range(n):
            mat[s][i] += mat[t][i]
            mat[i][s] = mat[s][i]
        mat[0][t] = float('-inf')
    
    return (int(best_weight), best_cut)

