"""
Fast Modulo in Python
======================

The C++ FastMod uses Barrett reduction with __uint128_t for ultra-fast modulo
operations. Python doesn't have this low-level optimization, but here are alternatives:

Method 1: Native Python (Simple, usually sufficient)
-----------------------------------------------------
```python
# Python's modulo is already quite optimized
result = a % b
```

Method 2: Barrett Reduction (For repeated mods by same constant)
-----------------------------------------------------------------
```python
class FastMod:
    '''Barrett reduction for fast modulo with constant divisor'''
    
    def __init__(self, b: int):
        self.b = b
        # Precompute m = floor(2^64 / b)
        self.m = (1 << 64) // b
    
    def reduce(self, a: int) -> int:
        '''Compute a % b quickly'''
        # q = floor(a * m / 2^64)
        q = (a * self.m) >> 64
        # a - q * b is in range [0, 2*b)
        r = a - q * self.b
        return r if r < self.b else r - self.b

# Usage
fm = FastMod(1000000007)
result = fm.reduce(12345678901234567890)
```

Method 3: Precomputed Powers (For modular exponentiation)
----------------------------------------------------------
```python
def mod_pow(base: int, exp: int, mod: int) -> int:
    '''Fast modular exponentiation'''
    result = 1
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result
```

Method 4: NumPy (For bulk operations)
--------------------------------------
```python
import numpy as np

# For arrays of numbers
arr = np.array([1000000, 2000000, 3000000])
result = arr % 1000000007
```

Performance Notes:
------------------
- Python's native % is implemented in C and is quite fast
- Barrett reduction helps when doing millions of mods by the same constant
- For competitive programming, native % is usually sufficient
- The C++ version is ~5x faster, but Python's % is rarely the bottleneck

When to use FastMod:
--------------------
- Only if profiling shows modulo is a bottleneck
- When doing > 10^7 modulo operations with same divisor
- In most cases, native Python % is fine

Example benchmark:
```python
import time

# Native modulo
start = time.time()
for i in range(10000000):
    _ = i % 1000000007
print(f"Native: {time.time() - start:.3f}s")

# FastMod
fm = FastMod(1000000007)
start = time.time()
for i in range(10000000):
    _ = fm.reduce(i)
print(f"FastMod: {time.time() - start:.3f}s")
```
"""

