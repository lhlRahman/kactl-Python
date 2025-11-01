"""
Author: Simon Lindholm
Date: 2018-07-18
License: CC0
Source: https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
Description: Runs a callback for all maximal cliques in a graph (given as a
symmetric adjacency matrix). Callback is given a set representing the maximal clique.
Time: O(3^{n/3}), much faster for sparse graphs
Status: stress-tested
"""

from typing import List, Set, Callable

def maximal_cliques(eds: List[Set[int]], f: Callable[[Set[int]], None], 
                    P: Set[int] = None, X: Set[int] = None, R: Set[int] = None):
    """
    Find all maximal cliques using Bron-Kerbosch algorithm.
    eds[i] = set of neighbors of node i
    f = callback function called with each maximal clique
    """
    if P is None:
        P = set(range(len(eds)))
    if X is None:
        X = set()
    if R is None:
        R = set()
    
    if not P:
        if not X:
            f(R)
        return
    
    # Choose pivot from P ∪ X
    pivot = next(iter(P | X))
    
    # Iterate through P \ N(pivot)
    cands = P - eds[pivot]
    for v in list(cands):
        maximal_cliques(eds, f, P & eds[v], X & eds[v], R | {v})
        P.remove(v)
        X.add(v)

