"""
Memory Optimization in Python
==============================

C++ has BumpAllocator, SmallPtr, and other memory optimization techniques.
Python manages memory differently, but here are equivalent optimizations:

1. Object Pooling (Similar to BumpAllocator)
---------------------------------------------
```python
class ObjectPool:
    '''Reuse objects instead of allocating new ones'''
    def __init__(self, factory, initial_size=100):
        self.factory = factory
        self.pool = [factory() for _ in range(initial_size)]
        self.in_use = []
    
    def acquire(self):
        if self.pool:
            obj = self.pool.pop()
        else:
            obj = self.factory()
        self.in_use.append(obj)
        return obj
    
    def release(self, obj):
        self.in_use.remove(obj)
        self.pool.append(obj)
    
    def release_all(self):
        self.pool.extend(self.in_use)
        self.in_use.clear()

# Usage
class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None

pool = ObjectPool(Node, 1000)
node1 = pool.acquire()
node2 = pool.acquire()
# ... use nodes ...
pool.release(node1)
pool.release(node2)
```

2. __slots__ (Reduce Memory per Object)
----------------------------------------
```python
# Without __slots__: each object has a __dict__
class NodeNormal:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# With __slots__: ~40% less memory
class NodeOptimized:
    __slots__ = ['value', 'left', 'right']
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# This prevents dynamic attribute creation but saves memory
```

3. Array Module (Similar to SmallPtr - compact storage)
--------------------------------------------------------
```python
import array

# Instead of list of ints (8 bytes each + overhead)
normal_list = [1, 2, 3, 4, 5]  # ~200 bytes

# Use array for compact storage (4 bytes each)
compact_array = array.array('i', [1, 2, 3, 4, 5])  # ~80 bytes

# For large datasets:
import numpy as np
compact_numpy = np.array([1, 2, 3, 4, 5], dtype=np.int32)  # Most compact
```

4. Generator Expressions (Lazy Evaluation)
-------------------------------------------
```python
# Bad: Creates entire list in memory
squares = [x*x for x in range(10000000)]

# Good: Generates values on demand
squares = (x*x for x in range(10000000))

# Usage
for sq in squares:
    if sq > 1000:
        break  # Early exit without computing all values
```

5. sys.intern() for String Deduplication
-----------------------------------------
```python
import sys

# Without interning: duplicate strings take separate memory
strings = [str(i % 100) for i in range(10000)]  # Many duplicates

# With interning: identical strings share memory
strings = [sys.intern(str(i % 100)) for i in range(10000)]
```

6. Weak References (Automatic Cleanup)
---------------------------------------
```python
import weakref

class Cache:
    def __init__(self):
        self.cache = weakref.WeakValueDictionary()
    
    def get(self, key):
        return self.cache.get(key)
    
    def set(self, key, value):
        self.cache[key] = value
    
    # Objects are automatically removed when no longer referenced elsewhere
```

7. Memory-Mapped Files (For Large Data)
----------------------------------------
```python
import mmap

# Instead of loading entire file into memory
with open('large_file.dat', 'r+b') as f:
    mmapped = mmap.mmap(f.fileno(), 0)
    # Access as if in memory, but OS handles paging
    data = mmapped[1000:2000]
```

8. Custom Memory Allocator Pattern
-----------------------------------
```python
class Arena:
    '''Allocate many small objects from pre-allocated blocks'''
    def __init__(self, size=1000000):
        self.buffer = bytearray(size)
        self.offset = 0
    
    def allocate(self, size):
        if self.offset + size > len(self.buffer):
            raise MemoryError("Arena full")
        start = self.offset
        self.offset += size
        return memoryview(self.buffer[start:start+size])
    
    def reset(self):
        self.offset = 0

# Usage for many small allocations
arena = Arena()
chunk1 = arena.allocate(100)
chunk2 = arena.allocate(200)
# ... use chunks ...
arena.reset()  # Reuse all memory
```

Performance Tips:
-----------------
1. Use __slots__ for classes with many instances
2. Use NumPy arrays instead of lists for numerical data
3. Use generators instead of lists when possible
4. Pre-allocate lists with known size: `[None] * n`
5. Use `bytearray` for mutable byte data
6. Pool frequently created/destroyed objects
7. Use `sys.getsizeof()` to measure actual memory usage

Measurement:
------------
```python
import sys
import tracemalloc

# Start tracking memory
tracemalloc.start()

# Your code here
data = [i for i in range(10000)]

# Get current memory usage
current, peak = tracemalloc.get_traced_memory()
print(f"Current: {current / 1024 / 1024:.2f} MB")
print(f"Peak: {peak / 1024 / 1024:.2f} MB")

tracemalloc.stop()
```

Conclusion:
-----------
Python abstracts away manual memory management, but you can still optimize
memory usage with __slots__, array/numpy, generators, and object pooling.
For competitive programming, these optimizations are rarely needed unless
working with very large datasets.
"""

