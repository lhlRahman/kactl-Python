"""
Author: chilli, SJTU, Janez Konc
Date: 2019-05-10
License: GPL3+
Source: Wikipedia, https://gitlab.com/janezkonc/mcqd
Description: Quickly finds a maximum clique of a graph (given as adjacency
matrix). Can be used to find a maximum independent set by finding a clique
of the complement graph.
Time: Runs in about 1s for n=155 and worst case random graphs (p=.90).
Runs faster for sparse graphs.
Status: stress-tested
"""

from typing import List

class MaxClique:
    """Find maximum clique in undirected graph"""
    
    def __init__(self, edges: List[List[bool]]):
        """
        Initialize with adjacency matrix.
        edges[i][j] = True if edge between i and j exists
        """
        self.limit = 0.025
        self.pk = 0
        self.e = edges
        self.n = len(edges)
        
        self.V = [{'i': i, 'd': 0} for i in range(self.n)]
        self.C = [[] for _ in range(self.n + 1)]
        self.qmax = []
        self.q = []
        self.S = [0] * (self.n + 1)
        self.old = [0] * (self.n + 1)
    
    def _init(self, R: List[dict]):
        """Initialize vertex degrees"""
        for v in R:
            v['d'] = 0
        
        for v in R:
            for u in R:
                if self.e[v['i']][u['i']]:
                    v['d'] += 1
        
        R.sort(key=lambda x: x['d'], reverse=True)
        
        mxD = R[0]['d'] if R else 0
        for i, v in enumerate(R):
            v['d'] = min(i, mxD) + 1
    
    def _expand(self, R: List[dict], lev: int = 1):
        """Expand current clique"""
        self.S[lev] += self.S[lev - 1] - self.old[lev]
        self.old[lev] = self.S[lev - 1]
        
        while R:
            if len(self.q) + R[-1]['d'] <= len(self.qmax):
                return
            
            self.q.append(R[-1]['i'])
            
            # Build neighbors of current vertex
            T = []
            for v in R:
                if self.e[R[-1]['i']][v['i']]:
                    T.append({'i': v['i'], 'd': 0})
            
            if T:
                self.S[lev] += 1
                self.pk += 1
                if self.S[lev] / self.pk < self.limit:
                    self._init(T)
                
                j = 0
                mxk = 1
                mnk = max(len(self.qmax) - len(self.q) + 1, 1)
                
                self.C[1].clear()
                self.C[2].clear()
                
                for v in T:
                    k = 1
                    # Find smallest color class that v doesn't conflict with
                    while any(self.e[v['i']][c] for c in self.C[k]):
                        k += 1
                    
                    if k > mxk:
                        mxk = k
                        if mxk + 1 < len(self.C):
                            self.C[mxk + 1].clear()
                    
                    if k < mnk:
                        if j < len(T):
                            T[j] = {'i': v['i'], 'd': 0}
                        else:
                            T.append({'i': v['i'], 'd': 0})
                        j += 1
                    
                    self.C[k].append(v['i'])
                
                if j > 0:
                    T[j - 1]['d'] = 0
                
                for k in range(mnk, mxk + 1):
                    for i in self.C[k]:
                        if j < len(T):
                            T[j] = {'i': i, 'd': k}
                        else:
                            T.append({'i': i, 'd': k})
                        j += 1
                
                T = T[:j]
                self._expand(T, lev + 1)
            
            elif len(self.q) > len(self.qmax):
                self.qmax = self.q[:]
            
            self.q.pop()
            R.pop()
    
    def max_clique(self) -> List[int]:
        """Find maximum clique. Returns list of vertex indices."""
        self._init(self.V)
        self._expand(self.V[:])
        return self.qmax

