"""
Test for LCA
Converted from stress-tests/graph/LCA.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from graph.lca import LCA
from graph.binary_lifting import tree_jump, lca as bin_lca
from test_utils import gen_random_tree

def get_parents_and_depth(tree, cur, p, d, par, depth):
    """Helper to compute parent and depth arrays"""
    par[cur] = p
    depth[cur] = d
    for i in tree[cur]:
        if i != p:
            get_parents_and_depth(tree, i, cur, d + 1, par, depth)

def test_n(n, num):
    """Test LCA with trees of size n"""
    for _ in range(num):
        graph = gen_random_tree(n)
        tree = [[] for _ in range(n)]
        
        for i, j in graph:
            tree[i].append(j)
            tree[j].append(i)
        
        par = [0] * n
        depth = [0] * n
        get_parents_and_depth(tree, 0, 0, 0, par, depth)
        
        tbl = tree_jump(par)
        new_lca = LCA(tree)
        
        for _ in range(100):
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)
            bin_lca_result = bin_lca(tbl, depth, a, b)
            new_lca_result = new_lca.lca(a, b)
            assert bin_lca_result == new_lca_result, f"Mismatch: bin={bin_lca_result}, new={new_lca_result}"

def test_lca():
    """Run all LCA tests"""
    random.seed(42)
    test_n(10, 1000)
    test_n(100, 100)
    test_n(1000, 10)
    print("Tests passed!")

if __name__ == "__main__":
    test_lca()

