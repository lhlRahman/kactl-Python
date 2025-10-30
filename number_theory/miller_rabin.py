"""
Author: chilli, c1729, Simon Lindholm
Date: 2019-03-28
License: CC0
Source: Wikipedia, https://miller-rabin.appspot.com/
Description: Deterministic Miller-Rabin primality test.
Guaranteed to work for numbers up to 7*10^18; for larger numbers, use Python and extend A randomly.
Time: 7 times the complexity of a^b mod c.
Status: Stress-tested
"""

from .mod_mul_ll import modpow

def is_prime(n: int) -> bool:
    """Deterministic Miller-Rabin primality test"""
    if n < 2 or n % 6 % 4 != 1:
        return (n | 1) == 3
    
    A = [2, 325, 9375, 28178, 450775, 9780504, 1795265022]
    s = (n - 1) & -(n - 1)  # count trailing zeroes: isolate lowest set bit
    s = s.bit_length() - 1  # convert to count
    d = n >> s
    
    for a in A:
        p = modpow(a % n, d, n)
        i = s
        while p != 1 and p != n - 1 and a % n and i:
            p = (p * p) % n
            i -= 1
        if p != n - 1 and i != s:
            return False
    return True

