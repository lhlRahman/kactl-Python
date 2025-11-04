"""
Fast Input in Python
====================

The C++ FastInput is a low-level optimization that doesn't translate directly to Python.
However, Python has several ways to optimize input reading:

Method 1: sys.stdin (Fastest for competitive programming)
-----------------------------------------------------------
```python
import sys
input = sys.stdin.readline

# Read single integer
n = int(input())

# Read list of integers
arr = list(map(int, input().split()))

# Read multiple values
a, b, c = map(int, input().split())
```

Method 2: sys.stdin.buffer (Even faster for bulk reading)
----------------------------------------------------------
```python
import sys
data = sys.stdin.buffer.read().decode().split()
ptr = 0

def read_int():
    global ptr
    ptr += 1
    return int(data[ptr - 1])

# Usage
n = read_int()
arr = [read_int() for _ in range(n)]
```

Method 3: Pre-read all input (Fastest for known input size)
------------------------------------------------------------
```python
import sys
lines = sys.stdin.read().split('\\n')
idx = 0

def next_line():
    global idx
    result = lines[idx]
    idx += 1
    return result

# Usage
n = int(next_line())
for _ in range(n):
    a, b = map(int, next_line().split())
```

Performance Comparison:
- input() [built-in]: ~1x
- sys.stdin.readline: ~2-3x faster
- sys.stdin.buffer: ~3-5x faster
- Pre-reading all: ~5-10x faster

For most competitive programming, Method 1 (sys.stdin.readline) provides
the best balance of speed and convenience.

Note: Always remember to flush output if using interactive problems:
    print(answer, flush=True)
"""

