"""
Bump Allocator in Python
=========================

The C++ BumpAllocator overrides the new operator to allocate from a
pre-allocated buffer, avoiding per-allocation overhead.

C++ BumpAllocator Pattern:
---------------------------
```cpp
static char buf[450 << 20];
void* operator new(size_t s) {
    static size_t i = sizeof buf;
    assert(s < i);
    return (void*)&buf[i -= s];
}
void operator delete(void*) {}
```

Why This Doesn't Apply to Python:
----------------------------------
1. Python manages memory automatically with reference counting and GC
2. No manual new/delete operators
3. Object allocation overhead is already optimized by the interpreter
4. Python's memory allocator is sophisticated (uses arenas, pools, etc.)

Python Equivalents:
-------------------

1. Object Pooling (Closest Equivalent)
---------------------------------------
```python
class BumpAllocator:
    '''Pre-allocate objects and reuse them'''
    
    def __init__(self, factory, size=10000):
        self.pool = [factory() for _ in range(size)]
        self.index = 0
    
    def alloc(self):
        if self.index >= len(self.pool):
            raise MemoryError("Pool exhausted")
        obj = self.pool[self.index]
        self.index += 1
        return obj
    
    def reset(self):
        '''Reset allocator to reuse all objects'''
        self.index = 0

# Usage
class Node:
    def __init__(self):
        self.value = 0
        self.left = None
        self.right = None

allocator = BumpAllocator(Node, 1000000)

# Allocate many nodes quickly
nodes = [allocator.alloc() for _ in range(10000)]

# Reuse memory
allocator.reset()
more_nodes = [allocator.alloc() for _ in range(10000)]
```

2. Pre-allocated Arrays (NumPy)
--------------------------------
```python
import numpy as np

class ArrayAllocator:
    '''Allocate slices from pre-allocated array'''
    
    def __init__(self, size):
        self.buffer = np.empty(size, dtype=np.float64)
        self.offset = 0
    
    def alloc(self, n):
        '''Allocate array of size n'''
        if self.offset + n > len(self.buffer):
            raise MemoryError("Buffer exhausted")
        result = self.buffer[self.offset:self.offset + n]
        self.offset += n
        return result
    
    def reset(self):
        self.offset = 0

# Usage
alloc = ArrayAllocator(1000000)
arr1 = alloc.alloc(100)  # Get slice of 100 elements
arr2 = alloc.alloc(200)  # Get slice of 200 elements
alloc.reset()  # Reuse buffer
```

3. memoryview for Zero-Copy Slicing
------------------------------------
```python
class ByteAllocator:
    '''Allocate from pre-allocated byte buffer'''
    
    def __init__(self, size):
        self.buffer = bytearray(size)
        self.offset = 0
    
    def alloc(self, size):
        '''Allocate byte slice'''
        if self.offset + size > len(self.buffer):
            raise MemoryError("Buffer exhausted")
        start = self.offset
        self.offset += size
        return memoryview(self.buffer[start:start + size])
    
    def reset(self):
        self.offset = 0

# Usage
alloc = ByteAllocator(1000000)
chunk1 = alloc.alloc(1000)  # Get 1000 bytes
chunk2 = alloc.alloc(2000)  # Get 2000 bytes
```

4. Arena Allocator Pattern
---------------------------
```python
class Arena:
    '''Arena-style allocator for Python objects'''
    
    def __init__(self):
        self.objects = []
    
    def alloc(self, factory):
        '''Allocate object using factory function'''
        obj = factory()
        self.objects.append(obj)
        return obj
    
    def clear(self):
        '''Clear all allocated objects'''
        self.objects.clear()
    
    def __enter__(self):
        return self
    
    def __exit__(self, *args):
        self.clear()

# Usage with context manager
with Arena() as arena:
    nodes = [arena.alloc(Node) for _ in range(1000)]
    # Use nodes...
# All nodes automatically cleared
```

Performance Comparison:
-----------------------
```python
import time

class SimpleNode:
    def __init__(self):
        self.value = 0
        self.next = None

# 1. Standard allocation
start = time.time()
nodes = [SimpleNode() for _ in range(1000000)]
print(f"Standard: {time.time() - start:.3f}s")

# 2. With object pool
pool = BumpAllocator(SimpleNode, 1000000)
start = time.time()
nodes = [pool.alloc() for _ in range(1000000)]
print(f"Pooled: {time.time() - start:.3f}s")

# Results: Pooling can be 2-3x faster for allocation-heavy code
```

When to Use Object Pooling:
----------------------------
1. Creating millions of short-lived objects
2. Known maximum number of objects needed
3. Objects can be reused/reset efficiently
4. Profiling shows allocation is a bottleneck

Example: Particle System
-------------------------
```python
class Particle:
    __slots__ = ['x', 'y', 'vx', 'vy', 'active']
    
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.x = self.y = 0.0
        self.vx = self.vy = 0.0
        self.active = False

class ParticleSystem:
    def __init__(self, max_particles=10000):
        # Pre-allocate all particles
        self.particles = [Particle() for _ in range(max_particles)]
        self.active_count = 0
    
    def emit(self, x, y, vx, vy):
        '''Emit a particle (reuse from pool)'''
        for p in self.particles:
            if not p.active:
                p.x, p.y = x, y
                p.vx, p.vy = vx, vy
                p.active = True
                self.active_count += 1
                return p
        return None  # Pool exhausted
    
    def update(self, dt):
        '''Update all active particles'''
        for p in self.particles:
            if p.active:
                p.x += p.vx * dt
                p.y += p.vy * dt
                # Deactivate if out of bounds, etc.

# Usage
system = ParticleSystem(10000)
for _ in range(100):
    system.emit(0, 0, 1, 1)
system.update(0.016)
```

Conclusion:
-----------
Python doesn't need manual memory allocators like C++. However, object
pooling can provide significant speedups for allocation-heavy workloads.
Use it judiciously and only after profiling shows it's beneficial.

For most competitive programming scenarios, Python's default memory
management is sufficient. Focus on algorithmic optimization instead.
"""

