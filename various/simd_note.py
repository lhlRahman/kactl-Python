"""
SIMD (Single Instruction Multiple Data) in Python
===================================================

The C++ SIMD code uses Intel SSE/AVX intrinsics for vectorized operations.
Python doesn't have direct access to these low-level instructions, but there
are several alternatives:

Method 1: NumPy (Recommended for numerical computing)
------------------------------------------------------
NumPy uses SIMD under the hood and is highly optimized.

```python
import numpy as np

# Vectorized operations (automatically use SIMD when available)
a = np.array([1, 2, 3, 4, 5, 6, 7, 8], dtype=np.int32)
b = np.array([8, 7, 6, 5, 4, 3, 2, 1], dtype=np.int32)

# Element-wise operations (SIMD optimized)
c = a + b
d = a * b
e = np.maximum(a, b)
f = np.sum(a)

# Dot product (highly optimized)
dot_product = np.dot(a, b)
```

Method 2: Numba (JIT compilation with SIMD)
--------------------------------------------
Numba can auto-vectorize loops and generate SIMD instructions.

```python
from numba import jit, vectorize, int32

@jit(nopython=True, fastmath=True)
def filtered_dot_product(a, b):
    '''Compute sum of a[i] * b[i] where a[i] < b[i]'''
    result = 0
    for i in range(len(a)):
        if a[i] < b[i]:
            result += a[i] * b[i]
    return result

# Numba will vectorize this if possible
a = np.array([1, 2, 3, 4], dtype=np.int32)
b = np.array([4, 3, 2, 1], dtype=np.int32)
result = filtered_dot_product(a, b)
```

Method 3: Direct SIMD with python-simd (experimental)
------------------------------------------------------
```python
# Requires: pip install simd
import simd

# This is experimental and platform-specific
```

Method 4: Cython with SIMD hints
---------------------------------
```python
# In a .pyx file
import numpy as np
cimport numpy as np
from cython cimport boundscheck, wraparound

@boundscheck(False)
@wraparound(False)
def fast_sum(np.ndarray[np.int32_t, ndim=1] arr):
    cdef int i
    cdef long long total = 0
    for i in range(arr.shape[0]):
        total += arr[i]
    return total
```

Performance Comparison:
-----------------------
- Pure Python loops: Baseline (1x)
- NumPy vectorized: 10-100x faster (uses SIMD automatically)
- Numba JIT: 10-200x faster (can generate optimal SIMD code)
- C++ SSE/AVX: Fastest, but requires C extension

Best Practices for Performance:
--------------------------------
1. Use NumPy for array operations (it's already SIMD-optimized)
2. Use Numba for custom algorithms that need to be fast
3. Avoid Python loops over large arrays
4. Use vectorized operations whenever possible

Example: Fast Dot Product with Filtering
-----------------------------------------
```python
import numpy as np

def filtered_dot_numpy(a, b):
    '''NumPy version - automatically uses SIMD'''
    mask = a < b
    return np.sum(a[mask] * b[mask])

# Or even simpler:
def filtered_dot_simple(a, b):
    return np.sum(np.where(a < b, a * b, 0))

# Usage
a = np.array([1, 2, 3, 4, 5], dtype=np.int16)
b = np.array([5, 4, 3, 2, 1], dtype=np.int16)
result = filtered_dot_numpy(a, b)
print(f"Result: {result}")
```

When to Use Each Method:
-------------------------
- NumPy: Default choice for any numerical work
- Numba: When you need custom loops but want C-like speed
- Pure Python: Only for small datasets or when clarity is paramount
- C extension: Only if profiling shows it's necessary and nothing else works

Conclusion:
-----------
While Python doesn't expose SIMD intrinsics directly, NumPy and Numba provide
excellent performance by using SIMD under the hood. For competitive programming
and algorithm contests, NumPy is usually sufficient and much easier to use than
manual SIMD programming.
"""

