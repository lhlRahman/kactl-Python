"""
Author: Simon Lindholm
Date: 2015-03-15
License: CC0
Source: own work
Description: Self-explanatory methods for string hashing.
Status: stress-tested
"""

from typing import List

# Using simple modulo for Python version
# In Python, we can use native integers which handle large numbers well
MOD = (1 << 64) - 1  # 2^64 - 1
C = int(1e11) + 3  # base for hashing

class H:
    """Hash value with arithmetic mod 2^64-1"""
    def __init__(self, x: int = 0):
        self.x = x % MOD
    
    def __add__(self, o):
        result = (self.x + o.x) % MOD
        return H(result)
    
    def __sub__(self, o):
        result = (self.x - o.x) % MOD
        return H(result)
    
    def __mul__(self, o):
        result = (self.x * o.x) % MOD
        return H(result)
    
    def get(self) -> int:
        return self.x
    
    def __eq__(self, o):
        return self.get() == o.get()
    
    def __lt__(self, o):
        return self.get() < o.get()
    
    def __hash__(self):
        return hash(self.x)

class HashInterval:
    """Compute hashes for all prefixes of a string"""
    def __init__(self, s: str):
        n = len(s)
        self.ha = [H(0) for _ in range(n + 1)]
        self.pw = [H(0) for _ in range(n + 1)]
        self.pw[0] = H(1)
        
        for i in range(n):
            self.ha[i + 1] = self.ha[i] * H(C) + H(ord(s[i]))
            self.pw[i + 1] = self.pw[i] * H(C)
    
    def hash_interval(self, a: int, b: int) -> H:
        """Hash substring [a, b)"""
        return self.ha[b] - self.ha[a] * self.pw[b - a]

def get_hashes(s: str, length: int) -> List[H]:
    """Get rolling hashes of all substrings of given length"""
    if len(s) < length:
        return []
    
    h = H(0)
    pw = H(1)
    for i in range(length):
        h = h * H(C) + H(ord(s[i]))
        pw = pw * H(C)
    
    ret = [h]
    for i in range(length, len(s)):
        h = h * H(C) + H(ord(s[i])) - pw * H(ord(s[i - length]))
        ret.append(h)
    
    return ret

def hash_string(s: str) -> H:
    """Compute hash of entire string"""
    h = H(0)
    for c in s:
        h = h * H(C) + H(ord(c))
    return h

