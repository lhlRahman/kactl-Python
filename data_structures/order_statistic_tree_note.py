"""
Order Statistic Tree in Python
================================

The C++ OrderStatisticTree uses GNU Policy-Based Data Structures (PBDS),
which is not available in Python. However, Python has several alternatives:

Method 1: SortedContainers (Recommended)
-----------------------------------------
```python
from sortedcontainers import SortedList

class OrderStatisticTree:
    def __init__(self):
        self.tree = SortedList()
    
    def insert(self, x):
        '''Insert element x'''
        self.tree.add(x)
    
    def remove(self, x):
        '''Remove element x'''
        self.tree.remove(x)
    
    def find_by_order(self, k):
        '''Find k-th smallest element (0-indexed)'''
        return self.tree[k] if 0 <= k < len(self.tree) else None
    
    def order_of_key(self, x):
        '''Count elements strictly less than x'''
        return self.tree.bisect_left(x)
    
    def lower_bound(self, x):
        '''Find first element >= x'''
        idx = self.tree.bisect_left(x)
        return self.tree[idx] if idx < len(self.tree) else None

# Usage
tree = OrderStatisticTree()
tree.insert(8)
tree.insert(10)
print(tree.order_of_key(10))  # 1
print(tree.find_by_order(0))  # 8
```

Method 2: Custom Treap Implementation
--------------------------------------
See treap.py in data_structures/ for a full implementation.

Method 3: bisect module (For simple cases)
-------------------------------------------
```python
import bisect

class SimpleOST:
    def __init__(self):
        self.items = []
    
    def insert(self, x):
        bisect.insort(self.items, x)
    
    def find_by_order(self, k):
        return self.items[k]
    
    def order_of_key(self, x):
        return bisect.bisect_left(self.items, x)
```

Performance Comparison:
- SortedContainers: O(log n) for all operations, highly optimized
- Custom Treap: O(log n) expected, good for learning
- bisect: O(n) insert, O(log n) search - only for small datasets

Installation:
```bash
pip install sortedcontainers
```

For competitive programming, SortedContainers is the best choice.
It's pure Python, fast, and well-tested.
"""

