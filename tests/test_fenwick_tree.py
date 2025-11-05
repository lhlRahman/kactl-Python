"""
Test for FenwickTree
Converted from stress-tests/data-structures/FenwickTree.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from data_structures.fenwick_tree import FenwickTree

def test_fenwick_tree():
    """Test FenwickTree with random operations"""
    for it in range(100000):
        N = random.randint(0, 10)
        if N == 0:
            continue
        fw = FenwickTree(N)
        t = [0] * N
        
        for i in range(N):
            v = random.randint(0, 3)
            fw.update(i, v)
            t[i] += v
        
        q = random.randint(0, 20)
        ind = fw.lower_bound(q)
        res = -1
        sum_val = 0
        for i in range(N + 1):
            if sum_val < q:
                res = i
            if i != N:
                sum_val += t[i]
        assert res == ind, f"Expected {res}, got {ind}"
    
    print("Tests passed!")

if __name__ == "__main__":
    random.seed(42)
    test_fenwick_tree()

