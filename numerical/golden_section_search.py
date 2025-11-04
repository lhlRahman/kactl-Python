"""
Author: Ulf Lundstrom
Date: 2009-04-17
License: CC0
Source: Numeriska algoritmer med matlab, Gerd Eriksson, NADA, KTH
Description: Finds the argument minimizing the function f in the interval [a,b]
assuming f is unimodal on the interval, i.e. has only one local minimum and no
local maximum. The maximum error in the result is eps. Works equally well for
maximization with a small change in the code.
Time: O(log((b-a) / epsilon))
Status: tested
"""

import math
from typing import Callable

def golden_section_search(a: float, b: float, f: Callable[[float], float], 
                         eps: float = 1e-7, maximize: bool = False) -> float:
    """
    Find minimum (or maximum) of unimodal function f on [a, b].
    a, b = interval boundaries
    f = function to minimize/maximize
    eps = precision
    maximize = if True, find maximum instead of minimum
    Returns x value that minimizes/maximizes f
    """
    # Golden ratio constant
    r = (math.sqrt(5) - 1) / 2
    
    x1 = b - r * (b - a)
    x2 = a + r * (b - a)
    f1 = f(x1)
    f2 = f(x2)
    
    while b - a > eps:
        if (f1 < f2) if not maximize else (f1 > f2):
            b = x2
            x2 = x1
            f2 = f1
            x1 = b - r * (b - a)
            f1 = f(x1)
        else:
            a = x1
            x1 = x2
            f1 = f2
            x2 = a + r * (b - a)
            f2 = f(x2)
    
    return a

# Example usage
if __name__ == "__main__":
    # Find minimum of f(x) = 4 + x + 0.3*x^2
    def func(x):
        return 4 + x + 0.3 * x * x
    
    xmin = golden_section_search(-1000, 1000, func)
    print(f"Minimum at x = {xmin:.6f}, f(x) = {func(xmin):.6f}")
    
    # Find maximum of f(x) = -(x-2)^2
    def parabola(x):
        return -(x - 2) ** 2
    
    xmax = golden_section_search(-10, 10, parabola, maximize=True)
    print(f"Maximum at x = {xmax:.6f}, f(x) = {parabola(xmax):.6f}")
