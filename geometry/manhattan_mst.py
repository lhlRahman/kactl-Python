"""
Author: chilli, Takanori MAEHARA
Date: 2019-11-02
License: CC0
Source: https://github.com/spaghetti-source/algorithm
Description: Given N points, returns up to 4*N edges, which are guaranteed
to contain a minimum spanning tree for the graph with edge weights w(p, q) =
|p.x - q.x| + |p.y - q.y|. Edges are in the form (distance, src, dst). Use a
standard MST algorithm on the result to find the final MST.
Time: O(N log N)
Status: Stress-tested
"""

from typing import List, Tuple
from .point import Point

def manhattan_mst(ps: List[Point]) -> List[Tuple[int, int, int]]:
    """
    Find candidate edges for Manhattan MST.
    ps = list of points
    Returns list of (distance, src_idx, dst_idx) edges
    """
    n = len(ps)
    ps = ps[:]  # Copy
    id_list = list(range(n))
    edges = []
    
    for k in range(4):
        # Sort by x - y
        id_list.sort(key=lambda i: ps[i].x - ps[i].y)
        
        sweep = {}  # y -> point index
        for i in id_list:
            # Find points that could form edges
            keys_to_remove = []
            for y_key in sorted(sweep.keys()):
                if y_key < -ps[i].y:
                    continue
                
                j = sweep[y_key]
                d = ps[i] - ps[j]
                if d.y > d.x:
                    break
                edges.append((d.y + d.x, i, j))
                keys_to_remove.append(y_key)
            
            for key in keys_to_remove:
                del sweep[key]
            
            sweep[-ps[i].y] = i
        
        # Transform points for next iteration
        if k & 1:
            for p in ps:
                p.x = -p.x
        else:
            for p in ps:
                p.x, p.y = p.y, p.x
    
    return edges

