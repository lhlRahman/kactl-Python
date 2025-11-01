"""
Author: chilli, Takanori MAEHARA, Benq, Simon Lindholm
Date: 2019-05-10
License: CC0
Source: https://github.com/spaghetti-source/algorithm
Description: Finds a minimum spanning tree/arborescence of a directed graph,
given a root node. If no MST exists, returns -1.
Time: O(E log V)
Status: Stress-tested, also tested on NWERC 2018 fastestspeedrun
"""

from typing import List, Tuple, Optional
from collections import deque
from ..data_structures.union_find_rollback import RollbackUnionFind

class Edge:
    def __init__(self, a: int, b: int, w: int):
        self.a = a  # source
        self.b = b  # destination
        self.w = w  # weight

class HeapNode:
    """Lazy skew heap node"""
    def __init__(self, key: Edge):
        self.key = key
        self.l: Optional[HeapNode] = None
        self.r: Optional[HeapNode] = None
        self.delta = 0
    
    def prop(self):
        """Propagate lazy delta"""
        self.key.w += self.delta
        if self.l:
            self.l.delta += self.delta
        if self.r:
            self.r.delta += self.delta
        self.delta = 0
    
    def top(self) -> Edge:
        self.prop()
        return self.key

def merge_heaps(a: Optional[HeapNode], b: Optional[HeapNode]) -> Optional[HeapNode]:
    """Merge two skew heaps"""
    if not a or not b:
        return a if a else b
    
    a.prop()
    b.prop()
    
    if a.key.w > b.key.w:
        a, b = b, a
    
    a.l, a.r = merge_heaps(b, a.r), a.l
    return a

def pop_heap(a: HeapNode) -> Optional[HeapNode]:
    """Pop minimum from heap"""
    a.prop()
    return merge_heaps(a.l, a.r)

def directed_mst(n: int, r: int, edges: List[Edge]) -> Tuple[int, List[int]]:
    """
    Find minimum spanning arborescence rooted at r.
    n = number of nodes
    r = root node
    edges = list of directed edges
    Returns (cost, parent_array) or (-1, []) if impossible
    """
    uf = RollbackUnionFind(n)
    heap = [None] * n
    
    # Build heap for each node
    for e in edges:
        heap[e.b] = merge_heaps(heap[e.b], HeapNode(e))
    
    res = 0
    seen = [-1] * n
    path = [0] * n
    par = [0] * n
    seen[r] = r
    
    Q = [None] * n
    in_edge = [Edge(-1, -1, 0)] * n
    cycs = deque()
    
    for s in range(n):
        u = s
        qi = 0
        
        while seen[u] < 0:
            if not heap[u]:
                return (-1, [])
            
            e = heap[u].top()
            heap[u].delta -= e.w
            heap[u] = pop_heap(heap[u])
            
            Q[qi] = e
            path[qi] = u
            qi += 1
            seen[u] = s
            res += e.w
            u = uf.find(e.a)
            
            if seen[u] == s:
                # Found cycle, contract it
                cyc_heap = None
                end = qi
                time = uf.time()
                
                while True:
                    w = path[qi - 1]
                    qi -= 1
                    cyc_heap = merge_heaps(cyc_heap, heap[w])
                    if not uf.join(u, w):
                        break
                
                u = uf.find(u)
                heap[u] = cyc_heap
                seen[u] = -1
                cycs.appendleft((u, time, Q[qi:end]))
        
        # Record incoming edges
        for i in range(qi):
            in_edge[uf.find(Q[i].b)] = Q[i]
    
    # Restore solution
    for u, t, comp in cycs:
        uf.rollback(t)
        in_e = in_edge[u]
        for e in comp:
            in_edge[uf.find(e.b)] = e
        in_edge[uf.find(in_e.b)] = in_e
    
    for i in range(n):
        par[i] = in_edge[i].a
    
    return (res, par)

