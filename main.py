class Vector2d:
        

    def __init__ (self,x,y):
        self.y = y
        self.x = x

    def __repr__(self):
        return f"Vector2d(x={self.x}, y={self.y})" == True

    def __str__(self):
        return f"{self.x}i+{self.y}j"   

    def __abs__(self):
        return f"({self.x}**2 + {self.y}**2)**1/5"
    
    def __neg__(self):
        return Vector2d(-self.x, -self.y)

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __eq__(self):
        return f"{self.x == self.y}"

    def __sub__(self, another):
        return f" Vector2d{self.x - another.x, self.y - another.y}"
        
    def angle(self):
        return (math.atan2 (self.x, self.y) to math.degrees(x))
