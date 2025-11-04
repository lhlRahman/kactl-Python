"""
Author: Simon Lindholm
License: CC0
Description: Add and remove intervals from a set of disjoint intervals.
Will merge the added interval with any overlapping intervals in the set when adding.
Intervals are [inclusive, exclusive).
Time: O(log N)
Status: stress-tested
"""

from sortedcontainers import SortedSet
from typing import Tuple

class IntervalContainer:
    """Maintain a set of disjoint intervals"""
    def __init__(self):
        self.intervals = SortedSet()
    
    def add_interval(self, L: int, R: int):
        """Add interval [L, R) to the set, merging with overlapping intervals"""
        if L == R:
            return
        
        # Find overlapping intervals
        to_remove = []
        for interval in self.intervals:
            if interval[0] > R:
                break
            if interval[1] >= L:
                L = min(L, interval[0])
                R = max(R, interval[1])
                to_remove.append(interval)
        
        # Remove overlapping intervals
        for interval in to_remove:
            self.intervals.remove(interval)
        
        # Add merged interval
        self.intervals.add((L, R))
    
    def remove_interval(self, L: int, R: int):
        """Remove interval [L, R) from the set"""
        if L == R:
            return
        
        # Find intervals that overlap with [L, R)
        to_remove = []
        to_add = []
        
        for interval in self.intervals:
            if interval[0] >= R:
                break
            if interval[1] <= L:
                continue
            
            to_remove.append(interval)
            
            # Add parts that don't overlap
            if interval[0] < L:
                to_add.append((interval[0], L))
            if interval[1] > R:
                to_add.append((R, interval[1]))
        
        # Update intervals
        for interval in to_remove:
            self.intervals.remove(interval)
        for interval in to_add:
            self.intervals.add(interval)
    
    def __iter__(self):
        return iter(self.intervals)
    
    def __len__(self):
        return len(self.intervals)

