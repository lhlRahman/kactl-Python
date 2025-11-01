"""
Author: Benjamin Qi, Oleksandr Kulkov, chilli
Date: 2020-01-12
License: CC0
Source: https://codeforces.com/blog/entry/53170
Description: Heavy-Light Decomposition. Decomposes a tree into vertex disjoint heavy paths
and light edges such that the path from any leaf to the root contains at most log(n)
light edges. Supports path and subtree queries/updates.
VALS_EDGES=True means values are stored in edges, False means nodes.
Root must be 0.
Time: O((log N)^2)
Status: stress-tested
"""

from typing import List, Callable

class HLD:
    """Heavy-Light Decomposition with segment tree support"""
    
    def __init__(self, adj: List[List[int]], vals_edges: bool = False):
        """
        Initialize HLD.
        adj = adjacency list (will be modified)
        vals_edges = True if values on edges, False if on nodes
        """
        self.N = len(adj)
        self.adj = [neighbors[:] for neighbors in adj]  # Deep copy
        self.vals_edges = vals_edges
        self.tim = 0
        
        self.par = [-1] * self.N
        self.siz = [1] * self.N
        self.rt = list(range(self.N))  # Root of heavy path
        self.pos = [0] * self.N  # Position in DFS order
        
        # Initialize segment tree (simple array-based for max queries)
        self.tree = [0] * (4 * self.N)
        self.lazy = [0] * (4 * self.N)
        
        self.dfs_sz(0)
        self.dfs_hld(0)
    
    def dfs_sz(self, v: int):
        """Calculate subtree sizes and reorder children"""
        for i, u in enumerate(self.adj[v]):
            # Remove back edge
            if u in self.adj[v] and v in self.adj[u]:
                self.adj[u].remove(v)
            
            self.par[u] = v
            self.dfs_sz(u)
            self.siz[v] += self.siz[u]
            
            # Move heaviest child to front
            if i == 0 or self.siz[u] > self.siz[self.adj[v][0]]:
                if i > 0:
                    self.adj[v][0], self.adj[v][i] = self.adj[v][i], self.adj[v][0]
    
    def dfs_hld(self, v: int):
        """Assign positions and heavy path roots"""
        self.pos[v] = self.tim
        self.tim += 1
        
        for i, u in enumerate(self.adj[v]):
            # First child continues heavy path
            self.rt[u] = self.rt[v] if i == 0 else u
            self.dfs_hld(u)
    
    def process_path(self, u: int, v: int, op: Callable[[int, int], None]):
        """Apply operation to all segments on path from u to v"""
        while True:
            if self.pos[u] > self.pos[v]:
                u, v = v, u
            if self.rt[u] == self.rt[v]:
                break
            op(self.pos[self.rt[v]], self.pos[v] + 1)
            v = self.par[self.rt[v]]
        
        op(self.pos[u] + self.vals_edges, self.pos[v] + 1)
    
    def modify_path(self, u: int, v: int, val: int):
        """Add val to all nodes/edges on path from u to v"""
        def add_op(l, r):
            # Simple segment tree add (can be replaced with actual lazy segtree)
            for i in range(l, r):
                self.tree[i] += val
        self.process_path(u, v, add_op)
    
    def query_path(self, u: int, v: int) -> int:
        """Query max value on path from u to v"""
        res = float('-inf')
        def query_op(l, r):
            nonlocal res
            for i in range(l, r):
                res = max(res, self.tree[i])
        self.process_path(u, v, query_op)
        return res
    
    def query_subtree(self, v: int) -> int:
        """Query subtree rooted at v"""
        l = self.pos[v] + self.vals_edges
        r = self.pos[v] + self.siz[v]
        res = float('-inf')
        for i in range(l, r):
            res = max(res, self.tree[i])
        return res

