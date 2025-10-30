"""
Author: Lukas Polacek
Date: 2009-09-28
License: CC0
Source: folklore
Description: Class for modular arithmetic operations.
You need to set mod to some number first and then you can use the structure.
"""

from .euclid import euclid

class Mod:
    """Modular arithmetic class"""
    mod = 10**9 + 7  # Default modulus, change as needed
    
    def __init__(self, x: int):
        self.x = x % self.mod
    
    def __add__(self, other: 'Mod') -> 'Mod':
        return Mod((self.x + other.x) % self.mod)
    
    def __sub__(self, other: 'Mod') -> 'Mod':
        return Mod((self.x - other.x + self.mod) % self.mod)
    
    def __mul__(self, other: 'Mod') -> 'Mod':
        return Mod((self.x * other.x) % self.mod)
    
    def __truediv__(self, other: 'Mod') -> 'Mod':
        return self * other.invert()
    
    def invert(self) -> 'Mod':
        """Modular inverse"""
        g, x, y = euclid(self.x, self.mod)
        assert g == 1, "Modular inverse does not exist"
        return Mod((x + self.mod) % self.mod)
    
    def __pow__(self, e: int) -> 'Mod':
        """Modular exponentiation"""
        if e == 0:
            return Mod(1)
        r = self ** (e // 2)
        r = r * r
        return self * r if e & 1 else r
    
    def __repr__(self) -> str:
        return f"Mod({self.x})"
    
    def __int__(self) -> int:
        return self.x

# Usage example:
# Mod.mod = 1000000007
# a = Mod(5)
# b = Mod(3)
# c = a + b  # 8
# d = a * b  # 15
# e = a / b  # modular division

