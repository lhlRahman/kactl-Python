"""
Author: Simon Lindholm
Date: 2017-05-10
License: CC0
Source: Wikipedia
Description: Given n points (x[i], y[i]), computes an n-1-degree polynomial p that
passes through them: p(x) = a[0]*x^0 + ... + a[n-1]*x^{n-1}.
For numerical precision, pick x[k] = c*cos(k/(n-1)*pi), k=0 ... n-1.
Time: O(n^2)
"""

from typing import List

def poly_interpolate(x: List[float], y: List[float], n: int) -> List[float]:
    """
    Interpolate polynomial through n points.
    x, y = lists of coordinates
    Returns coefficients [a0, a1, ..., a_{n-1}]
    """
    res = [0.0] * n
    temp = [0.0] * n
    y = y[:]  # Copy to avoid modifying input
    
    for k in range(n - 1):
        for i in range(k + 1, n):
            y[i] = (y[i] - y[k]) / (x[i] - x[k])
    
    last = 0.0
    temp[0] = 1.0
    
    for k in range(n):
        for i in range(n):
            res[i] += y[k] * temp[i]
            last, temp[i] = temp[i], temp[i] - last * x[k]
    
    return res

