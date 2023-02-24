import math
class Vector2d:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    def __repr__(self):
        return f"Vector2d(x={self.x}, y={self.y})"
    
    def __str__(self):
        return "Vector2d(self.x=xi,self.y=yj)"
    
    def __abs__(self):
        return "Vector2d(self.x**.5, self.y**.5)"
    
    def __neg__(self):
        return Vector2d(-self.x,-self.y)
    
    def __add__(self,other):
        return Vector2d(self.x + other.x , self.y + other.y)
    
    def __eq__(self,other):
        while True:
            return "Vector2d({self.x} == other, {self.y} ==other)"
    
    def __sub__(self,other):
        return "Vector2d(Vector2d(self.x,self.y) - other(self.x,self.y))"
    
    def angle(self):
        return math.atan2(math.atan2(self.y,self.x))