"""
Author: Ulf Lundstrom
Date: 2009-08-03
License: CC0
Source: My head
Description: Basic operations on square matrices.
Usage: A = Matrix(3); A.d = [[1,2,3],[4,5,6],[7,8,9]]
       vec = [1,2,3]; vec = (A ** N) * vec
Status: tested
"""

from typing import List

class Matrix:
    def __init__(self, n: int):
        self.n = n
        self.d = [[0] * n for _ in range(n)]
    
    def __mul__(self, other):
        """Matrix multiplication or matrix-vector multiplication"""
        if isinstance(other, Matrix):
            result = Matrix(self.n)
            for i in range(self.n):
                for j in range(self.n):
                    for k in range(self.n):
                        result.d[i][j] += self.d[i][k] * other.d[k][j]
            return result
        elif isinstance(other, list):
            # Matrix-vector multiplication
            result = [0] * self.n
            for i in range(self.n):
                for j in range(self.n):
                    result[i] += self.d[i][j] * other[j]
            return result
        else:
            raise TypeError("Can only multiply Matrix by Matrix or list")
    
    def __pow__(self, p: int):
        """Matrix exponentiation"""
        assert p >= 0
        result = Matrix(self.n)
        # Identity matrix
        for i in range(self.n):
            result.d[i][i] = 1
        
        base = Matrix(self.n)
        base.d = [row[:] for row in self.d]
        
        while p:
            if p & 1:
                result = result * base
            base = base * base
            p >>= 1
        return result

