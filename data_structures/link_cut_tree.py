"""
Author: Simon Lindholm
Date: 2016-07-25
Source: https://github.com/ngthanhtrung23/ACM_Notebook_new
Description: Represents a forest of unrooted trees. You can add and remove
edges (as long as the result is still a forest), and check whether
two nodes are in the same tree.
Time: All operations take amortized O(log N).
Status: Stress-tested a bit for N <= 20
"""

from typing import Optional

class LCTNode:
    """Splay tree node for Link-Cut Tree"""
    
    def __init__(self):
        self.p: Optional[LCTNode] = None  # Parent in splay tree
        self.pp: Optional[LCTNode] = None  # Path parent
        self.c = [None, None]  # Children [left, right]
        self.flip = False  # Lazy flip flag
        self.fix()
    
    def fix(self):
        """Update parent pointers"""
        if self.c[0]:
            self.c[0].p = self
        if self.c[1]:
            self.c[1].p = self
    
    def push_flip(self):
        """Push down flip operation"""
        if not self.flip:
            return
        self.flip = False
        self.c[0], self.c[1] = self.c[1], self.c[0]
        if self.c[0]:
            self.c[0].flip = not self.c[0].flip
        if self.c[1]:
            self.c[1].flip = not self.c[1].flip
    
    def up(self) -> int:
        """Return which child this is of its parent (-1 if root)"""
        if not self.p:
            return -1
        return 1 if self.p.c[1] == self else 0
    
    def rot(self, i: int, b: int):
        """Rotate operation"""
        h = i ^ b
        x = self.c[i]
        y = x if b == 2 else x.c[h]
        z = y if b else x
        
        y.p = self.p
        if self.p:
            self.p.c[self.up()] = y
        
        self.c[i] = z.c[i ^ 1]
        if b < 2:
            x.c[h] = y.c[h ^ 1]
            y.c[h ^ 1] = x
        z.c[i ^ 1] = self
        
        self.fix()
        x.fix()
        y.fix()
        if self.p:
            self.p.fix()
        
        self.pp, y.pp = y.pp, self.pp
    
    def splay(self):
        """Splay this node to root"""
        self.push_flip()
        while self.p:
            if self.p.p:
                self.p.p.push_flip()
            self.p.push_flip()
            self.push_flip()
            
            c1 = self.up()
            c2 = self.p.up()
            if c2 == -1:
                self.p.rot(c1, 2)
            else:
                self.p.p.rot(c2, 0 if c1 != c2 else 1)
    
    def first(self):
        """Return minimum element, splayed to top"""
        self.push_flip()
        if self.c[0]:
            return self.c[0].first()
        self.splay()
        return self

class LinkCutTree:
    """Link-Cut Tree for dynamic forest connectivity"""
    
    def __init__(self, n: int):
        """Initialize with n nodes"""
        self.nodes = [LCTNode() for _ in range(n)]
    
    def link(self, u: int, v: int):
        """Add edge between u and v"""
        assert not self.connected(u, v), "Nodes already connected"
        self._make_root(self.nodes[u])
        self.nodes[u].pp = self.nodes[v]
    
    def cut(self, u: int, v: int):
        """Remove edge between u and v"""
        x = self.nodes[u]
        top = self.nodes[v]
        self._make_root(top)
        x.splay()
        
        # Check edge exists
        assert top == (x.pp if x.pp else x.c[0]), "Edge does not exist"
        
        if x.pp:
            x.pp = None
        else:
            x.c[0] = None
            if top:
                top.p = None
            x.fix()
    
    def connected(self, u: int, v: int) -> bool:
        """Check if u and v are in same tree"""
        nu = self._access(self.nodes[u]).first()
        nv = self._access(self.nodes[v]).first()
        return nu == nv
    
    def _make_root(self, u: LCTNode):
        """Make u the root of its represented tree"""
        self._access(u)
        u.splay()
        if u.c[0]:
            u.c[0].p = None
            u.c[0].flip = not u.c[0].flip
            u.c[0].pp = u
            u.c[0] = None
            u.fix()
    
    def _access(self, u: LCTNode) -> LCTNode:
        """Make path from u to root into single auxiliary tree"""
        u.splay()
        while u.pp:
            pp = u.pp
            pp.splay()
            u.pp = None
            if pp.c[1]:
                pp.c[1].p = None
                pp.c[1].pp = pp
            pp.c[1] = u
            pp.fix()
            u = pp
        return u

