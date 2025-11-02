"""
Author: Simon Lindholm
Date: 2015-02-18
License: CC0
Source: marian's (TC) code
Description: Aho-Corasick automaton, used for multiple pattern matching.
Initialize with AhoCorasick(patterns); the automaton start node will be at index 0.
find(word) returns for each position the index of the longest word that ends there, or -1 if none.
findAll(patterns, word) finds all words (up to N√N many if no duplicate patterns)
that start at each position (shortest first).
Duplicate patterns are allowed; empty patterns are not.
Time: construction takes O(26N), where N = sum of length of patterns.
find(x) is O(N), where N = length of x. findAll is O(NM).
Status: stress-tested
"""

from typing import List
from collections import deque

class AhoCorasick:
    ALPHA = 26
    FIRST = ord('A')  # Change this for different alphabets
    
    class Node:
        def __init__(self):
            self.back = 0
            self.next = [-1] * AhoCorasick.ALPHA
            self.start = -1
            self.end = -1
            self.nmatches = 0
    
    def __init__(self, patterns: List[str]):
        self.N = [self.Node()]
        self.backp = []
        
        # Insert all patterns
        for j, pattern in enumerate(patterns):
            self._insert(pattern, j)
        
        # Build failure links
        self.N[0].back = len(self.N)
        self.N.append(self.Node())
        self.N[-1].back = 0
        
        q = deque([0])
        while q:
            n = q.popleft()
            prev = self.N[n].back
            
            for i in range(self.ALPHA):
                ed = self.N[n].next[i]
                y = self.N[prev].next[i]
                
                if ed == -1:
                    self.N[n].next[i] = y
                else:
                    self.N[ed].back = y
                    if self.N[ed].end == -1:
                        self.N[ed].end = self.N[y].end
                    else:
                        self.backp[self.N[ed].start] = self.N[y].end
                    self.N[ed].nmatches += self.N[y].nmatches
                    q.append(ed)
    
    def _insert(self, s: str, j: int):
        assert s, "Empty patterns not allowed"
        n = 0
        for c in s:
            idx = ord(c) - self.FIRST
            m = self.N[n].next[idx]
            if m == -1:
                m = len(self.N)
                self.N[n].next[idx] = m
                self.N.append(self.Node())
            n = m
        
        if self.N[n].end == -1:
            self.N[n].start = j
        self.backp.append(self.N[n].end)
        self.N[n].end = j
        self.N[n].nmatches += 1
    
    def find(self, word: str) -> List[int]:
        """For each position, return index of longest pattern that ends there, or -1"""
        n = 0
        res = []
        for c in word:
            idx = ord(c) - self.FIRST
            n = self.N[n].next[idx]
            res.append(self.N[n].end)
        return res
    
    def find_all(self, patterns: List[str], word: str) -> List[List[int]]:
        """Find all patterns that start at each position"""
        r = self.find(word)
        res = [[] for _ in range(len(word))]
        for i in range(len(word)):
            ind = r[i]
            while ind != -1:
                res[i - len(patterns[ind]) + 1].append(ind)
                ind = self.backp[ind]
        return res

