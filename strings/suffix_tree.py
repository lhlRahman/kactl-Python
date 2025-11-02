"""
Author: Unknown
Date: 2017-05-15
Source: https://e-maxx.ru/algo/ukkonen
Description: Ukkonen's algorithm for online suffix tree construction.
Each node contains indices [l, r) into the string, and a list of child nodes.
Suffixes are given by traversals of this tree, joining [l, r) substrings.
The root is 0 (has l = -1, r = 0), non-existent children are -1.
To get a complete tree, append a dummy symbol -- otherwise it may contain
an incomplete path (still useful for substring matching).
Time: O(26N) for alphabet size 26
Status: stress-tested a bit
"""

class SuffixTree:
    """Ukkonen's suffix tree for pattern matching"""
    
    def __init__(self, s: str, alpha_size: int = 26):
        """
        Build suffix tree for string s.
        alpha_size = alphabet size (26 for lowercase letters)
        """
        N = len(s) * 2 + 10
        self.s = s
        self.alpha_size = alpha_size
        
        # Arrays for suffix tree structure
        self.t = [[-1] * alpha_size for _ in range(N)]  # transitions
        self.l = [0] * N  # left bound of substring
        self.r = [len(s)] * N  # right bound
        self.p = [0] * N  # parent
        self.s_link = [0] * N  # suffix link
        
        self.v = 0  # current node
        self.q = 0  # current position in edge
        self.m = 2  # next free node
        
        # Initialize root
        self.l[0] = self.l[1] = -1
        self.r[0] = self.r[1] = 0
        self.p[0] = self.p[1] = 0
        for c in range(alpha_size):
            self.t[1][c] = 0
        self.s_link[0] = 1
        
        # Build tree character by character
        for i, ch in enumerate(s):
            self._ukkonen_add(i, ord(ch) - ord('a'))
    
    def _ukkonen_add(self, i: int, c: int):
        """Add character at position i"""
        while True:  # suff label
            if self.r[self.v] <= self.q:
                if self.t[self.v][c] == -1:
                    self.t[self.v][c] = self.m
                    self.l[self.m] = i
                    self.p[self.m] = self.v
                    self.m += 1
                    self.v = self.s_link[self.v]
                    self.q = self.r[self.v]
                    continue
                self.v = self.t[self.v][c]
                self.q = self.l[self.v]
            
            if self.q == -1 or c == ord(self.s[self.q]) - ord('a'):
                self.q += 1
                return
            else:
                # Split edge
                self.l[self.m + 1] = i
                self.p[self.m + 1] = self.m
                self.l[self.m] = self.l[self.v]
                self.r[self.m] = self.q
                self.p[self.m] = self.p[self.v]
                self.t[self.m][c] = self.m + 1
                self.t[self.m][ord(self.s[self.q]) - ord('a')] = self.v
                self.l[self.v] = self.q
                self.p[self.v] = self.m
                self.t[self.p[self.m]][ord(self.s[self.l[self.m]]) - ord('a')] = self.m
                self.v = self.s_link[self.p[self.m]]
                self.q = self.l[self.m]
                
                while self.q < self.r[self.m]:
                    self.v = self.t[self.v][ord(self.s[self.q]) - ord('a')]
                    self.q += self.r[self.v] - self.l[self.v]
                
                if self.q == self.r[self.m]:
                    self.s_link[self.m] = self.v
                else:
                    self.s_link[self.m] = self.m + 2
                
                self.q = self.r[self.v] - (self.q - self.r[self.m])
                self.m += 2
                return
    
    @staticmethod
    def longest_common_substring(s1: str, s2: str) -> tuple:
        """
        Find longest common substring of s1 and s2.
        Returns (length, position_in_s1)
        """
        # Build suffix tree with separator
        combined = s1 + chr(ord('z') + 1) + s2 + chr(ord('z') + 2)
        st = SuffixTree(combined, 28)
        
        # DFS to find LCS
        best = (0, 0)
        
        def dfs(node, depth):
            nonlocal best
            # Check if this subtree contains both strings
            has_s1 = False
            has_s2 = False
            
            if st.l[node] <= len(s1) < st.r[node]:
                has_s1 = True
            if st.l[node] <= len(s1) + 1 + len(s2) < st.r[node]:
                has_s2 = True
            
            # Check children
            for c in range(st.alpha_size):
                if st.t[node][c] != -1:
                    child_has = dfs(st.t[node][c], depth + st.r[node] - st.l[node])
                    has_s1 |= child_has[0]
                    has_s2 |= child_has[1]
            
            if has_s1 and has_s2 and depth > best[0]:
                best = (depth, st.r[node] - depth)
            
            return (has_s1, has_s2)
        
        dfs(0, 0)
        return best

