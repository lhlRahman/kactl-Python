"""
Author: Simon Lindholm
Date: 2015-02-11
License: CC0
Source: Wikipedia
Description: Fast integration using an adaptive Simpson's rule.
Status: mostly untested
"""

from typing import Callable

def integrate_adaptive(a: float, b: float, f: Callable[[float], float], 
                      eps: float = 1e-8) -> float:
    """
    Adaptive Simpson's rule integration.
    a, b = integration bounds
    f = function to integrate
    eps = desired precision
    """
    
    def simpson(x, y):
        """Simpson's rule estimate"""
        mid = (x + y) / 2
        return (f(x) + 4 * f(mid) + f(y)) * (y - x) / 6
    
    def rec(x, y, eps_local, S):
        """Recursive adaptive integration"""
        mid = (x + y) / 2
        S1 = simpson(x, mid)
        S2 = simpson(mid, y)
        T = S1 + S2
        
        if abs(T - S) <= 15 * eps_local or y - x < 1e-10:
            return T + (T - S) / 15
        
        return (rec(x, mid, eps_local / 2, S1) + 
                rec(mid, y, eps_local / 2, S2))
    
    return rec(a, b, eps, simpson(a, b))

