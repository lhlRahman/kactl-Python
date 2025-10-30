"""
Author: Simon Lindholm
Date: 2016-08-31
License: CC0
Source: http://eli.thegreenplace.net/2009/03/07/computing-modular-square-roots-in-python/
Description: Tonelli-Shanks algorithm for modular square roots. Finds x s.t. x^2 = a (mod p) (-x gives the other solution).
Time: O(log^2 p) worst case, O(log p) for most p
Status: Tested for all a,p <= 10000
"""

from .mod_pow import modpow

def mod_sqrt(a: int, p: int) -> int:
    """
    Find x such that x^2 ≡ a (mod p), where p is prime
    Returns one solution; -x (mod p) is the other solution
    Raises assertion error if no solution exists
    """
    a %= p
    if a < 0:
        a += p
    if a == 0:
        return 0
    
    assert modpow(a, (p - 1) // 2, p) == 1, "No solution exists"
    
    if p % 4 == 3:
        return modpow(a, (p + 1) // 4, p)
    
    # Tonelli-Shanks algorithm
    s = p - 1
    r = 0
    while s % 2 == 0:
        r += 1
        s //= 2
    
    # Find a non-square mod p
    n = 2
    while modpow(n, (p - 1) // 2, p) != p - 1:
        n += 1
    
    x = modpow(a, (s + 1) // 2, p)
    b = modpow(a, s, p)
    g = modpow(n, s, p)
    
    while True:
        t = b
        m = 0
        while m < r and t != 1:
            t = t * t % p
            m += 1
        
        if m == 0:
            return x
        
        gs = modpow(g, 1 << (r - m - 1), p)
        g = gs * gs % p
        x = x * gs % p
        b = b * g % p
        r = m

