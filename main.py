class Vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2d(x={self.x},y = {self.y})"

    def __str__(self):
        return f"{self.x}i + {self.y}j"

    def __abs__(self):
        return str((int(self.x**2) + int(self.y**2))**.5)
    
    def __neg__(self):
        return f"Vector(-{self.x},-{self.y})"
    
    def __add__(self,other):
        return f"Vector2d({int(self.x) + int(other.x)},{int(self.y) + int(other.y)})"