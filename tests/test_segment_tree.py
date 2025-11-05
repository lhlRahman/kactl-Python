"""
Test for Segment Tree
Converted from stress-tests/data-structures/SegmentTree.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from data_structures.segment_tree import SegmentTree

def test_segment_tree():
    """Test segment tree with random operations"""
    random.seed(42)
    
    # Test empty tree
    t = SegmentTree(0, max, float('-inf'))
    assert t.query(0, 0) == t.unit
    
    # Test with random updates and queries
    for n in range(1, 10):
        tr = SegmentTree(n, max, float('-inf'))
        v = [float('-inf')] * n
        
        for it in range(1000):  # Reduced for faster testing
            i = random.randint(0, n)
            j = random.randint(0, n)
            x = random.randint(0, n + 1)
            
            r = random.randint(0, 99)
            if r < 30:
                # Query
                ma = float('-inf')
                for k in range(i, j):
                    ma = max(ma, v[k])
                result = tr.query(i, j)
                assert ma == result, f"Query failed: expected {ma}, got {result}"
            else:
                # Update
                i = min(i, n - 1)
                tr.update(i, x)
                v[i] = x
    
    print("Tests passed!")

if __name__ == "__main__":
    test_segment_tree()

