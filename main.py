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
    def __neg__(self): 
        return f"Vector2d({self.x * -1}, {self.y * -1})" 
    def __add__(self, other): 
        sum_x = self.x + other.x 
        sum_y = self.y + other.y 
        return f"Vector2d({sum_x},{sum_y})"
    
    
test = Vector2d(3,4) 
test1 = Vector2d(1,-1)