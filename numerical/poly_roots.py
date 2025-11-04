"""
Author: Per Austrin
Date: 2004-02-08
License: CC0
Description: Finds the real roots to a polynomial using recursive bisection.
Time: O(n^2 log(1/epsilon))
"""

from typing import List
from .polynomial import Polynomial

def poly_roots(p: Polynomial, xmin: float, xmax: float, eps: float = 1e-8) -> List[float]:
    """
    Find all real roots of polynomial p in interval [xmin, xmax].
    p = polynomial
    xmin, xmax = search interval
    eps = precision
    Returns list of roots
    """
    # Base case: linear polynomial
    if len(p.a) == 2:
        if abs(p.a[1]) > 1e-10:
            root = -p.a[0] / p.a[1]
            if xmin <= root <= xmax:
                return [root]
        return []
    
    # Find roots of derivative
    der = Polynomial(p.a[:])
    der.diff()
    dr = poly_roots(der, xmin, xmax, eps)
    
    # Add boundary points
    dr.append(xmin - 1)
    dr.append(xmax + 1)
    dr.sort()
    
    ret = []
    
    # Check each interval between critical points
    for i in range(len(dr) - 1):
        l = dr[i]
        h = dr[i + 1]
        
        # Check if both endpoints are in valid range
        if h < xmin or l > xmax:
            continue
        
        l = max(l, xmin)
        h = min(h, xmax)
        
        # Check if there's a sign change (root exists)
        fl = p(l)
        fh = p(h)
        
        if (fl > 0) != (fh > 0):
            # Binary search for root
            for _ in range(60):  # Enough iterations for machine precision
                m = (l + h) / 2
                fm = p(m)
                if (fm <= 0) == (fl > 0):
                    l = m
                    fl = fm
                else:
                    h = m
                    fh = fm
            
            ret.append((l + h) / 2)
    
    return ret

# Example usage
if __name__ == "__main__":
    # Solve x^2 - 3x + 2 = 0 (roots are 1 and 2)
    p = Polynomial([2, -3, 1])  # 2 - 3x + x^2
    roots = poly_roots(p, -1e9, 1e9)
    print(f"Roots of x^2 - 3x + 2: {roots}")
    
    # Solve x^3 - 6x^2 + 11x - 6 = 0 (roots are 1, 2, 3)
    p = Polynomial([-6, 11, -6, 1])
    roots = poly_roots(p, -10, 10)
    print(f"Roots of x^3 - 6x^2 + 11x - 6: {roots}")
