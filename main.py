class Vector2d:
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 
    def __repr__(self): 
        return f"Vector2d(x={self.x}, y={self.y})"
    def __str__(self): 
        return f"{self.x}i + {self.y}j"
    def __abs__(self):   
        c = self.x ** 2 + self.y ** 2
        return c ** (1/2)
    
test = Vector2d(3,4)