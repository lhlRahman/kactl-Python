"""
Author: User adamant on CodeForces
Source: http://codeforces.com/blog/entry/12143
Description: For each position in a string, computes p[0][i] = half length of
longest even palindrome around pos i, p[1][i] = longest odd (half rounded down).
Time: O(N)
Status: Stress-tested
"""

from typing import List

def manacher(s: str) -> List[List[int]]:
    """
    Returns [even_palindromes, odd_palindromes]
    even_palindromes[i] = half length of longest even palindrome centered at position i
    odd_palindromes[i] = half length (rounded down) of longest odd palindrome centered at position i
    """
    n = len(s)
    p = [[0] * (n + 1), [0] * n]
    
    for z in range(2):
        i = 0
        l = 0
        r = 0
        while i < n:
            t = r - i + (1 if z == 0 else 0)
            if i < r:
                p[z][i] = min(t, p[z][l + t])
            
            L = i - p[z][i]
            R = i + p[z][i] - (1 if z == 0 else 0)
            
            while L >= 1 and R + 1 < n and s[L - 1] == s[R + 1]:
                p[z][i] += 1
                L -= 1
                R += 1
            
            if R > r:
                l = L
                r = R
            
            i += 1
    
    return p

