"""
Hash Map in Python
==================

The C++ HashMap uses GNU PBDS (gp_hash_table) with custom hash function.
Python has excellent built-in dictionary support that's usually sufficient.

Method 1: Built-in dict (Recommended for most cases)
-----------------------------------------------------
```python
# Python's dict is highly optimized
h = {}
h[key] = value
val = h.get(key, default)
```

Method 2: collections.defaultdict
----------------------------------
```python
from collections import defaultdict

# Automatic default values
h = defaultdict(int)  # defaults to 0
h[key] += 1  # no KeyError

h = defaultdict(list)  # defaults to []
h[key].append(value)
```

Method 3: Custom Hash with salt (For competitive programming)
--------------------------------------------------------------
```python
import random
import sys

class FastHash:
    '''Hash map with custom hash to avoid hacking'''
    
    def __init__(self):
        self.RANDOM = random.randrange(2**62)
        self.data = {}
    
    def _hash(self, x):
        '''Custom hash function with random salt'''
        # Mix bits and add randomness
        x = (x ^ self.RANDOM) * 0xbf58476d1ce4e5b9
        x = (x ^ (x >> 30)) * 0x94d049bb133111eb
        return (x ^ (x >> 27)) & sys.maxsize
    
    def __setitem__(self, key, value):
        self.data[self._hash(key)] = (key, value)
    
    def __getitem__(self, key):
        h = self._hash(key)
        if h in self.data and self.data[h][0] == key:
            return self.data[h][1]
        raise KeyError(key)
    
    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

# Usage
h = FastHash()
h[12345] = 100
print(h[12345])  # 100
```

Method 4: Using hash() with salt (Simplest anti-hack)
------------------------------------------------------
```python
import random

RANDOM = random.randrange(2**32)

def custom_hash(x):
    return hash((x, RANDOM))

# Use with dict
h = {}
h[custom_hash(key)] = value
```

Performance Comparison:
-----------------------
- Python dict: O(1) average, highly optimized in CPython
- C++ gp_hash_table: ~3x faster than unordered_map in C++
- Python dict is slower than C++ but rarely the bottleneck

When to worry about hacking:
-----------------------------
- Codeforces and similar platforms where anti-hash tests exist
- Use RANDOM salt in hash function
- Python's hash() is already quite good with randomization

Example with timing-resistant hash:
```python
import time

class TimingResistantHash:
    def __init__(self):
        # Use time-based seed (like C++ version)
        self.seed = int(time.time() * 1000000) & 0xFFFFFFFF
        self.data = {}
    
    def _hash(self, x):
        return hash((x ^ self.seed, self.seed))
    
    def __setitem__(self, key, value):
        self.data[self._hash(key)] = value
    
    def __getitem__(self, key):
        return self.data[self._hash(key)]
```

Recommendation:
---------------
For 99% of cases, use Python's built-in dict. It's fast, reliable,
and has anti-collision measures built in. Only use custom hashing if:
1. You're on a platform known for anti-hash tests
2. You've profiled and dict is actually the bottleneck
"""

