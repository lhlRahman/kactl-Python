"""
Author: 罗穗骞, chilli
Date: 2019-04-11
License: Unknown
Source: Suffix array - a powerful tool for dealing with strings
(Chinese IOI National team training paper, 2009)
Description: Builds suffix array for a string.
sa[i] is the starting index of the suffix which is i'th in the sorted suffix array.
The returned vector is of size n+1, and sa[0] = n.
The lcp array contains longest common prefixes for neighbouring strings in the suffix array:
lcp[i] = lcp(sa[i], sa[i-1]), lcp[0] = 0.
The input string must not contain any nul chars.
Time: O(n log n)
Status: stress-tested
"""

from typing import List

class SuffixArray:
    def __init__(self, s: str, lim: int = 256):
        # Convert string to list and append null terminator
        s_list = [ord(c) for c in s] + [0]
        n = len(s_list)
        k = 0
        
        x = s_list[:]
        y = [0] * n
        ws = [0] * max(n, lim)
        
        self.sa = list(range(n))
        self.lcp = [0] * n
        
        j = 0
        p = 0
        while p < n:
            # Radix sort
            p = j
            y[p:p + n - j] = list(range(n - j, n))
            p += n - j
            for i in range(n):
                if self.sa[i] >= j:
                    y[p] = self.sa[i] - j
                    p += 1
            
            ws[:lim] = [0] * lim
            for i in range(n):
                ws[x[i]] += 1
            for i in range(1, lim):
                ws[i] += ws[i - 1]
            for i in range(n - 1, -1, -1):
                ws[x[y[i]]] -= 1
                self.sa[ws[x[y[i]]]] = y[i]
            
            x, y = y, x
            p = 1
            x[self.sa[0]] = 0
            for i in range(1, n):
                a = self.sa[i - 1]
                b = self.sa[i]
                if y[a] == y[b] and a + j < n and b + j < n and y[a + j] == y[b + j]:
                    x[b] = p - 1
                else:
                    x[b] = p
                    p += 1
            
            j = max(1, j * 2)
            lim = p
            if p >= n:
                break
        
        # Build LCP array
        for i in range(n - 1):
            if k:
                k -= 1
            j = self.sa[x[i] - 1]
            while i + k < n - 1 and j + k < n - 1 and s_list[i + k] == s_list[j + k]:
                k += 1
            self.lcp[x[i]] = k

