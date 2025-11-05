"""
Test for Z-function
Converted from stress-tests/strings/Zfunc.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from strings.zfunc import Z
import itertools

def test_z(s):
    """Test Z function against naive implementation"""
    n = len(s)
    found = Z(s)
    expected = [0] * n
    
    for i in range(1, n):  # exclude index 0
        j = 0
        while i + j < n and s[i + j] == s[j]:
            j += 1
        expected[i] = j
    
    assert found == expected, f"Failed for s={s}"

def test_zfunc():
    """Test Z-function with all strings up to certain lengths"""
    # Test ~3^12 strings
    for n in range(13):
        for combo in itertools.product('abc', repeat=n):
            s = ''.join(combo)
            test_z(s)
    
    # Test ~4^10 strings (subset)
    for n in range(11):
        for combo in itertools.product('abcd', repeat=n):
            s = ''.join(combo)
            test_z(s)
    
    print("Tests passed!")

if __name__ == "__main__":
    test_zfunc()

