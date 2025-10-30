"""
Author: Jakob Kogler, chilli, pajenegod
Date: 2020-04-12
License: CC0
Description: Prime sieve for generating all primes smaller than LIM.
Time: LIM=1e9 ≈ 1.5s
Status: Stress-tested
Details: Despite its n log log n complexity, segmented sieve is still faster
than other options due to low memory usage which reduces cache misses.
This implementation skips even numbers.
"""

import math
from typing import List

def fast_eratosthenes(LIM: int) -> List[int]:
    """
    Fast segmented sieve for generating primes up to LIM.
    Returns list of all primes < LIM.
    """
    S = int(math.sqrt(LIM))
    R = LIM // 2
    
    pr = [2]
    sieve = [False] * (S + 1)
    
    # Generate small primes
    for i in range(3, S + 1, 2):
        if not sieve[i]:
            for j in range(i * i, S + 1, 2 * i):
                sieve[j] = True
    
    # Collect small primes with their starting positions
    cp = []
    for i in range(3, S + 1, 2):
        if not sieve[i]:
            cp.append((i, i * i // 2))
    
    # Segmented sieve
    for L in range(1, R + 1, S):
        block = [False] * S
        
        for idx_pair in cp:
            p, idx = idx_pair[0], idx_pair[1]
            i = idx
            while i < S + L:
                if i - L >= 0 and i - L < S:
                    block[i - L] = True
                i += p
            # Update idx for next iteration
            cp[cp.index(idx_pair)] = (p, i)
        
        for i in range(min(S, R - L)):
            if not block[i]:
                pr.append((L + i) * 2 + 1)
    
    return pr

