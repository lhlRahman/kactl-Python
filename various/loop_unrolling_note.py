"""
Loop Unrolling in Python
=========================

The C++ Unrolling pattern manually unrolls loops for performance.
Python handles this differently:

C++ Unrolling Pattern:
----------------------
```cpp
#define F {...; ++i;}
int i = from;
while (i&3 && i < to) F // for alignment
while (i + 4 <= to) { F F F F }
while (i < to) F
```

Python Equivalents:
-------------------

1. NumPy (Automatically Optimized)
-----------------------------------
```python
import numpy as np

# Python loops are slow, but NumPy is fast (internally unrolled)
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
result = arr * 2 + 1  # Automatically vectorized and unrolled
```

2. Manual Unrolling (Rarely Needed)
------------------------------------
```python
def process_unrolled(data, func):
    '''Manually unroll loop by factor of 4'''
    i = 0
    n = len(data)
    
    # Process 4 at a time
    while i + 4 <= n:
        func(data[i])
        func(data[i + 1])
        func(data[i + 2])
        func(data[i + 3])
        i += 4
    
    # Handle remainder
    while i < n:
        func(data[i])
        i += 1

# Example
total = 0
def add_to_total(x):
    global total
    total += x

process_unrolled([1, 2, 3, 4, 5, 6, 7], add_to_total)
```

3. Numba (JIT Compilation with Auto-Unrolling)
-----------------------------------------------
```python
from numba import jit
import numpy as np

@jit(nopython=True)
def sum_array(arr):
    '''Numba may automatically unroll this loop'''
    total = 0
    for x in arr:
        total += x
    return total

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
result = sum_array(arr)  # Compiled to optimized machine code
```

4. itertools.islice for Chunked Processing
-------------------------------------------
```python
from itertools import islice

def process_chunks(data, chunk_size=4):
    '''Process data in chunks'''
    it = iter(data)
    while True:
        chunk = list(islice(it, chunk_size))
        if not chunk:
            break
        # Process chunk
        for item in chunk:
            process(item)
```

When Loop Unrolling Helps:
---------------------------
- C++: Can provide 10-30% speedup by reducing loop overhead
- Python: Native loops are already slow, unrolling doesn't help much
- Use NumPy or Numba instead of manual unrolling

Performance Comparison:
-----------------------
```python
import time
import numpy as np
from numba import jit

# Test data
n = 10000000
data = list(range(n))
arr = np.arange(n)

# 1. Pure Python loop (baseline)
start = time.time()
total = 0
for x in data:
    total += x
print(f"Python loop: {time.time() - start:.3f}s")

# 2. Manually unrolled Python loop
start = time.time()
total = 0
i = 0
while i + 4 <= n:
    total += data[i] + data[i+1] + data[i+2] + data[i+3]
    i += 4
while i < n:
    total += data[i]
    i += 1
print(f"Unrolled Python: {time.time() - start:.3f}s")  # Barely faster!

# 3. NumPy (automatically optimized)
start = time.time()
total = np.sum(arr)
print(f"NumPy: {time.time() - start:.3f}s")  # Much faster!

# 4. Numba (JIT compiled)
@jit(nopython=True)
def numba_sum(arr):
    return np.sum(arr)

start = time.time()
total = numba_sum(arr)
print(f"Numba: {time.time() - start:.3f}s")  # Fastest!
```

Results (typical):
- Python loop: 0.5s
- Unrolled Python: 0.48s (minimal improvement)
- NumPy: 0.01s (50x faster!)
- Numba: 0.005s (100x faster!)

Recommendation:
---------------
Don't manually unroll loops in Python. Instead:
1. Use NumPy for numerical computations
2. Use Numba for custom algorithms
3. Use list comprehensions for simple transformations
4. Profile before optimizing

Example of Pythonic Optimization:
----------------------------------
```python
# Bad: Manual unrolling
result = []
i = 0
while i + 4 <= len(data):
    result.append(func(data[i]))
    result.append(func(data[i+1]))
    result.append(func(data[i+2]))
    result.append(func(data[i+3]))
    i += 4
while i < len(data):
    result.append(func(data[i]))
    i += 1

# Good: Pythonic
result = [func(x) for x in data]

# Better: NumPy (if applicable)
result = np.vectorize(func)(np.array(data))

# Best: Numba (for custom logic)
@jit(nopython=True)
def process_all(data):
    result = np.empty(len(data))
    for i in range(len(data)):
        result[i] = func(data[i])
    return result
```

Conclusion:
-----------
Loop unrolling is a low-level C++ optimization that doesn't translate
well to Python. Python's interpreter overhead dominates, making manual
unrolling ineffective. Use NumPy or Numba for real performance gains.
"""

