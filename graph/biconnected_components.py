"""
Author: Simon Lindholm
Date: 2017-04-17
License: CC0
Source: folklore
Description: Finds all biconnected components in an undirected graph, and
runs a callback for the edges in each. In a biconnected component there
are at least two distinct paths between any two nodes. Note that a node can
be in several components. An edge which is not in a component is a bridge,
i.e., not part of any cycle.
Usage:
  ed = [[] for _ in range(N)]
  eid = 0
  for each edge (a,b):
    ed[a].append((b, eid))
    ed[b].append((a, eid))
    eid += 1
  bicomps(ed, lambda edgelist: ...)
Time: O(E + V)
Status: tested during MIPT ICPC Workshop 2017
"""

from typing import List, Tuple, Callable

def biconnected_components(ed: List[List[Tuple[int, int]]], callback: Callable[[List[int]], None]):
    """
    Find all biconnected components.
    ed[i] = list of (neighbor, edge_id) pairs
    callback is called with list of edge IDs for each biconnected component
    """
    num = [0] * len(ed)
    st = []
    time_counter = [0]
    
    def dfs(at: int, par: int) -> int:
        time_counter[0] += 1
        me = num[at] = time_counter[0]
        top = me
        
        for y, e in ed[at]:
            if e == par:
                continue
            
            if num[y]:
                top = min(top, num[y])
                if num[y] < me:
                    st.append(e)
            else:
                si = len(st)
                up = dfs(y, e)
                top = min(top, up)
                
                if up == me:
                    st.append(e)
                    callback(st[si:])
                    del st[si:]
                elif up < me:
                    st.append(e)
                # else: e is a bridge
        
        return top
    
    for i in range(len(ed)):
        if not num[i]:
            dfs(i, -1)

