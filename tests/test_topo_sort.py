"""
Test for TopoSort
Converted from stress-tests/graph/TopoSort.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from graph.topo_sort import topo_sort

def test_topo_sort():
    """Test topological sort with random graphs"""
    random.seed(42)
    for it in range(50000):
        n = random.randint(0, 20)
        m = random.randint(0, 30) if n else 0
        acyclic = random.choice([True, False])
        
        order = list(range(n))
        random.shuffle(order)
        ed = [[] for _ in range(n)]
        
        for i in range(m):
            a = random.randint(0, n - 1)
            b = random.randint(0, n - 1)
            if acyclic and a >= b:
                continue
            ed[order[a]].append(order[b])
        
        ret = topo_sort(ed)
        if acyclic:
            assert len(ret) == n, f"Expected {n} nodes, got {len(ret)}"
        else:
            assert len(ret) <= n
        
        seen = [False] * n
        for i in ret:
            assert not seen[i], f"Node {i} seen twice"
            seen[i] = True
            for j in ed[i]:
                assert not seen[j], f"Edge {i}->{j} goes forward"
    
    print("Tests passed!")

if __name__ == "__main__":
    test_topo_sort()

