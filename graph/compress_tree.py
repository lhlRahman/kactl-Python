"""
Author: Simon Lindholm
Date: 2016-01-14
License: CC0
Description: Given a rooted tree and a subset S of nodes, compute the minimal
subtree that contains all the nodes by adding all (at most |S|-1)
pairwise LCA's and compressing edges.
Returns a list of (parent, original_index) representing a tree rooted at 0.
The root points to itself.
Time: O(|S| log |S|)
Status: Tested at CodeForces
"""

from typing import List, Tuple

def compress_tree(lca_structure, subset: List[int]) -> List[Tuple[int, int]]:
    """
    Compress tree to minimal subtree containing subset.
    lca_structure = LCA object with lca() and time[] methods
    subset = list of node indices to include
    Returns list of (parent_in_compressed_tree, original_node_index)
    """
    if not subset:
        return []
    
    T = lca_structure.time
    li = sorted(subset, key=lambda x: T[x])
    
    # Add all pairwise LCAs
    m = len(li) - 1
    for i in range(m):
        a = li[i]
        b = li[i + 1]
        li.append(lca_structure.lca(a, b))
    
    # Remove duplicates and sort by DFS time
    li = sorted(set(li), key=lambda x: T[x])
    
    # Build reverse mapping
    rev = {node: i for i, node in enumerate(li)}
    
    # Build compressed tree
    ret = [(0, li[0])]  # Root points to itself
    for i in range(len(li) - 1):
        a = li[i]
        b = li[i + 1]
        lca_node = lca_structure.lca(a, b)
        ret.append((rev[lca_node], b))
    
    return ret

