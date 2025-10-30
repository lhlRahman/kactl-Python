"""
Author: Håkan Terelius
Date: 2009-09-25
License: CC0
Source: http://en.wikipedia.org/wiki/Euler's_totient_function
Description: Euler's φ function is defined as φ(n) := # of positive integers <= n that are coprime with n.
φ(1)=1, p prime => φ(p^k)=(p-1)p^(k-1), m,n coprime => φ(mn)=φ(m)φ(n).

Euler's thm: a,n coprime => a^φ(n) ≡ 1 (mod n).
Fermat's little thm: p prime => a^(p-1) ≡ 1 (mod p) for all a.
Status: Tested
"""

from typing import List

def calculate_phi(LIM: int) -> List[int]:
    """Calculate Euler's totient function for all numbers up to LIM"""
    phi = [i if i & 1 else i // 2 for i in range(LIM)]
    
    for i in range(3, LIM, 2):
        if phi[i] == i:  # i is prime
            for j in range(i, LIM, i):
                phi[j] -= phi[j] // i
    
    return phi

