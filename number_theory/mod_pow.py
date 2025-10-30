"""
Author: Noam527
Date: 2019-04-24
License: CC0
Source: folklore
Description: Modular exponentiation
Status: tested
"""

MOD = 1000000007  # faster if const

def modpow(b: int, e: int, mod: int = MOD) -> int:
    """Compute b^e mod mod"""
    ans = 1
    while e:
        if e & 1:
            ans = ans * b % mod
        b = b * b % mod
        e //= 2
    return ans

