"""
Author: Simon Lindholm
Date: 2015-03-15
License: CC0
Source: own work
Description: Various methods for string hashing with dual-modulo approach.
Use on Codeforces, which lacks 64-bit support and where solutions can be hacked.
Status: stress-tested
"""

import time

# Initialize random constant C (should be done once at startup)
C = int(time.time() * 1000000) % 1000000007

class Hash:
    """Dual-modulo hash for anti-hack protection"""
    MOD1 = 1000000007
    MOD2 = 1000000009
    
    def __init__(self, x=0, y=0):
        self.x = x % self.MOD1
        self.y = y % self.MOD2
    
    def __add__(self, other):
        x = (self.x + other.x) % self.MOD1
        y = (self.y + other.y) % self.MOD2
        return Hash(x, y)
    
    def __sub__(self, other):
        x = (self.x - other.x + self.MOD1) % self.MOD1
        y = (self.y - other.y + self.MOD2) % self.MOD2
        return Hash(x, y)
    
    def __mul__(self, other):
        x = (self.x * other.x) % self.MOD1
        y = (self.y * other.y) % self.MOD2
        return Hash(x, y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __hash__(self):
        return self.x ^ (self.y << 21)
    
    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)
    
    def __repr__(self):
        return f"Hash({self.x}, {self.y})"

class HashInterval:
    """Compute hash of any substring in O(1) after O(n) preprocessing"""
    
    def __init__(self, s: str):
        n = len(s)
        self.ha = [Hash(0, 0)] * (n + 1)
        self.pw = [Hash(0, 0)] * (n + 1)
        self.pw[0] = Hash(1, 1)
        
        for i in range(n):
            self.ha[i + 1] = self.ha[i] * Hash(C, C) + Hash(ord(s[i]), ord(s[i]))
            self.pw[i + 1] = self.pw[i] * Hash(C, C)
    
    def hash_interval(self, a: int, b: int) -> Hash:
        """Get hash of substring [a, b)"""
        return self.ha[b] - self.ha[a] * self.pw[b - a]

def get_hashes(s: str, length: int) -> list:
    """
    Get hashes of all substrings of given length.
    Returns list of Hash objects.
    """
    if len(s) < length:
        return []
    
    # Compute initial hash
    h = Hash(0, 0)
    pw = Hash(1, 1)
    for i in range(length):
        h = h * Hash(C, C) + Hash(ord(s[i]), ord(s[i]))
        pw = pw * Hash(C, C)
    
    ret = [h]
    
    # Rolling hash
    for i in range(length, len(s)):
        h = h * Hash(C, C) + Hash(ord(s[i]), ord(s[i])) - pw * Hash(ord(s[i - length]), ord(s[i - length]))
        ret.append(h)
    
    return ret

def hash_string(s: str) -> Hash:
    """Compute hash of entire string"""
    h = Hash(0, 0)
    for c in s:
        h = h * Hash(C, C) + Hash(ord(c), ord(c))
    return h

# Example usage:
if __name__ == "__main__":
    # Test HashInterval
    s = "abcabc"
    hi = HashInterval(s)
    
    h1 = hi.hash_interval(0, 3)  # "abc"
    h2 = hi.hash_interval(3, 6)  # "abc"
    assert h1 == h2
    
    # Test rolling hashes
    hashes = get_hashes("abcdef", 3)
    print(f"Found {len(hashes)} substrings of length 3")
    
    # Test string hash
    h = hash_string("hello")
    print(f"Hash of 'hello': {h}")

