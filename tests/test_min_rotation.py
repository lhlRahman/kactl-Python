"""
Test for MinRotation
Converted from stress-tests/strings/MinRotation.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from strings.min_rotation import min_rotation

def min_rotation_naive(v):
    """Naive O(n^2) implementation for verification"""
    n = len(v)
    w = v + v
    j = 0
    for i in range(1, n):
        if w[i:i+n] < w[j:j+n]:
            j = i
    return j

def test_min_rotation():
    """Test min_rotation with random strings"""
    random.seed(42)
    for it in range(100000):
        n = random.randint(0, 10)
        v = ''.join(chr(ord('a') + random.randint(0, 2)) for _ in range(n))
        r = min_rotation(v)
        r2 = min_rotation_naive(v)
        assert r == r2, f"Failed for v={v}: got {r}, expected {r2}"
        
        # After rotating by r, min rotation should be 0
        v_rotated = v[r:] + v[:r]
        assert min_rotation(v_rotated) == 0
        assert min_rotation_naive(v_rotated) == 0
    
    print("Tests passed!")

if __name__ == "__main__":
    test_min_rotation()

