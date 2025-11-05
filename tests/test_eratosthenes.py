"""
Test for Eratosthenes Sieve
Converted from stress-tests/number-theory/Eratosthenes.cpp
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from number_theory.eratosthenes import eratosthenes_sieve

def is_prime_naive(n):
    """Naive primality test for verification"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def test_eratosthenes():
    """Test Eratosthenes sieve"""
    # Test small cases
    for lim in range(2, 1000):
        pr = eratosthenes_sieve(lim)
        expected = [i for i in range(2, lim) if is_prime_naive(i)]
        assert pr == expected, f"Failed for lim={lim}"
    
    # Test larger case
    pr = eratosthenes_sieve(10000)
    for p in pr:
        assert is_prime_naive(p), f"{p} is not prime"
    
    # Verify count is reasonable (prime number theorem)
    assert len(pr) > 1000, "Should have > 1000 primes below 10000"
    
    print("Tests passed!")

if __name__ == "__main__":
    test_eratosthenes()

