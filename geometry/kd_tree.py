"""
Author: Stanford
Date: Unknown
Source: Stanford Notebook
Description: KD-tree for nearest neighbor search (2d, can be extended to 3d)
Status: Tested on excellentengineers
"""

from typing import List, Tuple, Optional
from .point import Point

class KDNode:
    """Node in KD-tree"""
    
    def __init__(self, points: List[Point]):
        self.pt = points[0]
        self.x0 = min(p.x for p in points)
        self.x1 = max(p.x for p in points)
        self.y0 = min(p.y for p in points)
        self.y1 = max(p.y for p in points)
        self.first = None
        self.second = None
        
        if len(points) > 1:
            # Split on x if width >= height
            if self.x1 - self.x0 >= self.y1 - self.y0:
                points.sort(key=lambda p: p.x)
            else:
                points.sort(key=lambda p: p.y)
            
            half = len(points) // 2
            self.first = KDNode(points[:half])
            self.second = KDNode(points[half:])
    
    def distance(self, p: Point) -> float:
        """Minimum squared distance from point p to this bounding box"""
        x = p.x if self.x0 <= p.x <= self.x1 else (self.x0 if p.x < self.x0 else self.x1)
        y = p.y if self.y0 <= p.y <= self.y1 else (self.y0 if p.y < self.y0 else self.y1)
        return (Point(x, y) - p).dist2()

class KDTree:
    """KD-tree for efficient nearest neighbor queries"""
    
    def __init__(self, points: List[Point]):
        """Build KD-tree from list of points"""
        self.root = KDNode(points[:])
    
    def _search(self, node: KDNode, p: Point) -> Tuple[float, Point]:
        """Recursively search for nearest point"""
        if node.first is None:
            # Leaf node
            return ((p - node.pt).dist2(), node.pt)
        
        # Search closer child first
        f, s = node.first, node.second
        bfirst = f.distance(p)
        bsec = s.distance(p)
        
        if bfirst > bsec:
            f, s = s, f
            bfirst, bsec = bsec, bfirst
        
        # Search closest side
        best = self._search(f, p)
        
        # Search other side if it might contain a closer point
        if bsec < best[0]:
            other = self._search(s, p)
            if other[0] < best[0]:
                best = other
        
        return best
    
    def nearest(self, p: Point) -> Tuple[float, Point]:
        """
        Find nearest point to p.
        Returns (squared_distance, nearest_point)
        """
        return self._search(self.root, p)

