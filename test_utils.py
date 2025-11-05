"""
Test utilities for generating random inputs and trees.
"""

import random
from typing import List, Tuple

def prufer_code_to_tree(prufer_code: List[int]) -> List[Tuple[int, int]]:
    """
    Convert Prufer Code to Tree
    Complexity: O(V log V)
    """
    node_count = {}
    leaves = set()
    
    length = len(prufer_code)
    node = length + 2
    
    # Count frequency of nodes
    for t in prufer_code:
        node_count[t] = node_count.get(t, 0) + 1
    
    # Find the absent nodes (leaves)
    for i in range(1, node + 1):
        if i not in node_count:
            leaves.add(i)
    
    edges = []
    
    # Connect edges
    for i in range(length):
        a = prufer_code[i]  # First node
        
        # Find the smallest number which is not present in prufer code now
        b = min(leaves)  # the leaf
        
        edges.append((a, b))  # Edge of the tree
        
        leaves.remove(b)  # Remove from absent list
        node_count[a] -= 1  # Remove from prufer code
        if node_count[a] == 0:
            leaves.add(a)  # If a becomes absent
    
    # The final edge
    leaves_list = sorted(leaves)
    edges.append((leaves_list[0], leaves_list[-1]))
    return edges

def gen_random_tree(n: int) -> List[Tuple[int, int]]:
    """Generate a random tree with n nodes (0-indexed)"""
    prufer_code = []
    for i in range(n - 2):
        prufer_code.append(random.randint(1, n - 1))
    edges = prufer_code_to_tree(prufer_code)
    # Convert to 0-indexed
    edges = [(p[0] - 1, p[1] - 1) for p in edges]
    return edges

