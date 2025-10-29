# Python KACTL - KTH Algorithm Competition Template Library

This is a Python port of KACTL (KTH's Algorithm Competition Template Library), converting C++ implementations to Python while maintaining correctness through comprehensive testing.

## Overview

Python KACTL provides optimized, tested implementations of competitive programming algorithms in Python. Each algorithm has been carefully converted from the original C++ version and tested to ensure correctness.

## Installation

No special installation required. Simply add the `python_kactl` directory to your Python path or copy the modules you need.

```python
import sys
sys.path.append('/path/to/python_kactl')

from data_structures.fenwick_tree import FenwickTree
from graph.lca import LCA
from number_theory.miller_rabin import is_prime
```

## Modules

### Data Structures
- **FenwickTree**: Binary Indexed Tree for range sum queries
- **FenwickTree2D**: 2D Fenwick Tree for 2D range queries
- **SegmentTree**: Segment tree for range queries with custom operations
- **RMQ**: Range Minimum Query with O(1) query time
- **UnionFind**: Disjoint Set Union with path compression

### Graph Algorithms
- **LCA**: Lowest Common Ancestor using RMQ
- **BinaryLifting**: Tree jumping for LCA and ancestor queries
- **BellmanFord**: Shortest paths with negative edges
- **FloydWarshall**: All-pairs shortest paths
- **TopoSort**: Topological sorting
- **SCC**: Strongly Connected Components (Tarjan's algorithm)

### Number Theory
- **Eratosthenes**: Prime sieve
- **Euclid**: Extended Euclidean algorithm
- **ModPow**: Fast modular exponentiation
- **MillerRabin**: Deterministic primality testing
- **Factor**: Prime factorization (Pollard-rho)
- **CRT**: Chinese Remainder Theorem
- **ModInverse**: Modular inverse computation
- **ModSum**: Sums of modded arithmetic progressions
- **PhiFunction**: Euler's totient function

### String Algorithms
- **KMP**: Knuth-Morris-Pratt pattern matching
- **Hashing**: String hashing with rolling hash
- **Z-function**: Z-algorithm for pattern matching
- **MinRotation**: Find lexicographically smallest rotation

### Geometry
- **Point**: 2D point class with vector operations
- **ConvexHull**: Convex hull in O(n log n)
- **PolygonArea**: Signed area of polygon

### Various
- **LIS**: Longest Increasing Subsequence
- **TernarySearch**: Find maximum of unimodal function

### Combinatorial
- **IntPerm**: Permutation to integer conversion

## Usage Examples

### Fenwick Tree
```python
from data_structures.fenwick_tree import FenwickTree

# Create a Fenwick tree of size 10
ft = FenwickTree(10)

# Update position 3 by adding 5
ft.update(3, 5)

# Query sum of [0, 7)
print(ft.query(7))

# Find position where cumulative sum >= 10
print(ft.lower_bound(10))
```

### LCA (Lowest Common Ancestor)
```python
from graph.lca import LCA

# adjacency list of tree (0-indexed)
tree = [[1, 2], [0, 3, 4], [0], [1], [1]]

lca = LCA(tree)
print(lca.lca(3, 4))  # Find LCA of nodes 3 and 4
```

### Miller-Rabin Primality Test
```python
from number_theory.miller_rabin import is_prime

print(is_prime(1000000007))  # True
print(is_prime(1000000009))  # True
print(is_prime(1000000000))  # False
```

### KMP Pattern Matching
```python
from strings.kmp import match

text = "ababcababa"
pattern = "aba"
matches = match(text, pattern)
print(matches)  # [0, 5, 7]
```

### Convex Hull
```python
from geometry.point import Point
from geometry.convex_hull import convex_hull

points = [Point(0, 0), Point(1, 1), Point(2, 0), Point(1, 2)]
hull = convex_hull(points)
print([str(p) for p in hull])
```

## Running Tests

All algorithms come with comprehensive stress tests converted from the original C++ test suite.

### Run all tests:
```bash
cd python_kactl
python run_all_tests.py
```

### Run specific test:
```bash
cd python_kactl
python tests/test_fenwick_tree.py
python tests/test_lca.py
python tests/test_miller_rabin.py
```

## Test Results

Current test status (all passing ✓):
- test_fenwick_tree.py ✓
- test_segment_tree.py ✓  
- test_lca.py ✓
- test_topo_sort.py ✓
- test_eratosthenes.py ✓
- test_miller_rabin.py ✓
- test_kmp.py ✓
- test_zfunc.py ✓
- test_min_rotation.py ✓

## Performance Notes

While Python is generally slower than C++, these implementations are optimized for Python:
- Uses native Python data structures efficiently
- Avoids unnecessary allocations
- Uses appropriate algorithms with good asymptotic complexity

For competitive programming, these implementations are suitable for:
- Educational purposes
- Prototyping solutions
- Problems with lenient time limits
- When Python is the preferred language

## Conversion Status

See [CONVERSION_STATUS.md](CONVERSION_STATUS.md) for detailed information about which algorithms have been converted and tested.

Currently converted: **35+ algorithms** across all major categories
All converted algorithms: **Thoroughly tested**

## Contributing

To add more algorithms:
1. Follow the existing code structure
2. Include docstrings with author, date, license, description, complexity, and status
3. Write comprehensive tests based on the C++ stress tests
4. Update CONVERSION_STATUS.md

## License

Same as original KACTL - mostly CC0 (public domain) where noted in individual files. Some algorithms have specific licenses noted in their headers.

## Acknowledgments

This is a Python port of [KACTL](https://github.com/kth-competitive-programming/kactl) by KTH Royal Institute of Technology. All credit for algorithm design and original implementations goes to the KACTL contributors.

## References

- Original KACTL: https://github.com/kth-competitive-programming/kactl
- KACTL PDF: See `../kactl.pdf` in the parent directory

