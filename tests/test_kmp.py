"""
Test for KMP algorithm
Converted from stress-tests/strings/KMP.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strings.kmp import pi
import itertools

def test_pi(s):
    """Test pi function against naive implementation"""
    p = pi(s)
    for i in range(len(s)):
        maxlen = -1
        for length in range(i + 1):
            match = True
            for j in range(length):
                if s[j] != s[i + 1 - length + j]:
                    match = False
                    break
            if match:
                maxlen = length
        assert maxlen == p[i], f"Failed for s={s}, i={i}: expected {maxlen}, got {p[i]}"

def test_kmp():
    """Test KMP with all strings up to certain lengths"""
    # Test ~3^12 strings
    for n in range(13):
        for combo in itertools.product('abc', repeat=n):
            s = ''.join(combo)
            test_pi(s)
    
    # Test ~4^10 strings (subset)
    for n in range(11):
        for combo in itertools.product('abcd', repeat=n):
            s = ''.join(combo)
            test_pi(s)
    
    print("Tests passed!")

if __name__ == "__main__":
    test_kmp()

