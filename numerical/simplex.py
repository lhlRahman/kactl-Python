"""
Author: Stanford
Source: Stanford Notebook
License: MIT
Description: Solves a general linear maximization problem: maximize c^T x subject to Ax <= b, x >= 0.
Returns -inf if there is no solution, inf if there are arbitrarily good solutions, or the maximum value of c^T x otherwise.
The input vector is set to an optimal x (or in the unbounded case, an arbitrary solution fulfilling the constraints).
Numerical stability is not guaranteed. For better performance, define variables such that x = 0 is viable.
Time: O(NM * #pivots), where a pivot may be e.g. an edge relaxation. O(2^n) in the general case.
Status: seems to work?
"""

from typing import List

EPS = 1e-8

class LPSolver:
    def __init__(self, A: List[List[float]], b: List[float], c: List[float]):
        """
        Initialize LP solver.
        A = constraint matrix
        b = constraint RHS
        c = objective function coefficients
        """
        self.m = len(b)
        self.n = len(c)
        self.N = list(range(self.n + 1))
        self.B = [self.n + i for i in range(self.m)]
        self.D = [[0.0] * (self.n + 2) for _ in range(self.m + 2)]
        
        for i in range(self.m):
            for j in range(self.n):
                self.D[i][j] = A[i][j]
            self.D[i][self.n] = -1
            self.D[i][self.n + 1] = b[i]
        
        for j in range(self.n):
            self.D[self.m][j] = -c[j]
        
        self.N[self.n] = -1
        self.D[self.m + 1][self.n] = 1
    
    def pivot(self, r: int, s: int):
        """Perform pivot operation"""
        inv = 1.0 / self.D[r][s]
        
        for i in range(self.m + 2):
            if i != r and abs(self.D[i][s]) > EPS:
                inv2 = self.D[i][s] * inv
                for j in range(self.n + 2):
                    self.D[i][j] -= self.D[r][j] * inv2
                self.D[i][s] = self.D[r][s] * inv2
        
        for j in range(self.n + 2):
            if j != s:
                self.D[r][j] *= inv
        
        for i in range(self.m + 2):
            if i != r:
                self.D[i][s] *= -inv
        
        self.D[r][s] = inv
        self.B[r], self.N[s] = self.N[s], self.B[r]
    
    def simplex(self, phase: int) -> bool:
        """Run simplex algorithm"""
        x = self.m + phase - 1
        while True:
            s = -1
            for j in range(self.n + 1):
                if self.N[j] != -phase:
                    if s == -1 or (self.D[x][j], self.N[j]) < (self.D[x][s], self.N[s]):
                        s = j
            
            if self.D[x][s] >= -EPS:
                return True
            
            r = -1
            for i in range(self.m):
                if self.D[i][s] <= EPS:
                    continue
                if r == -1 or (self.D[i][self.n + 1] / self.D[i][s], self.B[i]) < \
                              (self.D[r][self.n + 1] / self.D[r][s], self.B[r]):
                    r = i
            
            if r == -1:
                return False
            
            self.pivot(r, s)
    
    def solve(self) -> tuple:
        """
        Solve LP problem.
        Returns (optimal_value, optimal_x)
        """
        r = 0
        for i in range(1, self.m):
            if self.D[i][self.n + 1] < self.D[r][self.n + 1]:
                r = i
        
        if self.D[r][self.n + 1] < -EPS:
            self.pivot(r, self.n)
            if not self.simplex(2) or self.D[self.m + 1][self.n + 1] < -EPS:
                return (float('-inf'), [])
            
            for i in range(self.m):
                if self.B[i] == -1:
                    s = 0
                    for j in range(1, self.n + 1):
                        if s == -1 or (self.D[i][j], self.N[j]) < (self.D[i][s], self.N[s]):
                            s = j
                    self.pivot(i, s)
        
        ok = self.simplex(1)
        x = [0.0] * self.n
        for i in range(self.m):
            if self.B[i] < self.n:
                x[self.B[i]] = self.D[i][self.n + 1]
        
        return (self.D[self.m][self.n + 1] if ok else float('inf'), x)

