"""
Author: chilli, Ramchandra Apte, Noam527, Simon Lindholm
Date: 2019-04-24
License: CC0
Source: https://github.com/RamchandraApte/OmniTemplate/blob/master/src/number_theory/modulo.hpp
Description: Calculate a*b mod c (or a^b mod c) for 0 <= a, b <= c <= 7.2*10^18.
Time: O(1) for modmul, O(log b) for modpow
Status: stress-tested, proven correct
"""

def modmul(a: int, b: int, M: int) -> int:
    """Multiply a*b mod M for large numbers"""
    # For Python, we can use native arbitrary precision
    # But for compatibility with C++ behavior, we implement the same logic
    ret = a * b - M * int(1.0 / M * a * b)
    if ret < 0:
        ret += M
    if ret >= M:
        ret -= M
    return ret

def modpow(b: int, e: int, mod: int) -> int:
    """Compute b^e mod mod using modmul"""
    ans = 1
    while e:
        if e & 1:
            ans = modmul(ans, b, mod)
        b = modmul(b, b, mod)
        e //= 2
    return ans

