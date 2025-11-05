"""
Test for Miller-Rabin Primality Test
Converted from stress-tests/number-theory/MillerRabin.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import random
from number_theory.miller_rabin import is_prime
from number_theory.eratosthenes import eratosthenes_sieve

def test_miller_rabin():
    """Test Miller-Rabin primality test"""
    random.seed(42)
    
    # Test against sieve for small numbers
    MAXPR = 100000
    prs = eratosthenes_sieve(MAXPR)
    isprime_arr = [False] * MAXPR
    for p in prs:
        isprime_arr[p] = True
    
    for n in range(MAXPR):
        if is_prime(n) != isprime_arr[n]:
            print(f"fails for {n}")
            assert False
    
    # Test some known primes and composites
    known_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                    1009, 10007, 100003, 1000003, 10000019, 
                    999999937, 1000000007, 1000000009]
    for p in known_primes:
        assert is_prime(p), f"{p} should be prime"
    
    known_composites = [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20,
                        1000, 10000, 100000, 1000000,
                        999999999, 1000000000, 1000000001]
    for c in known_composites:
        assert not is_prime(c), f"{c} should be composite"
    
    # Test some large primes
    large_primes = [
        2147483647,  # 2^31 - 1 (Mersenne prime)
        1000000000039,
        1000000000061,
    ]
    for p in large_primes:
        assert is_prime(p), f"{p} should be prime"
    
    print("Tests passed!")

if __name__ == "__main__":
    test_miller_rabin()

