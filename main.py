class Vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Vector2d(x = {self.x}, y = {self.y})"
    def __str__(self):
        return "(self.x)i + {self.y}j"
    def __abs__(self):
         return h (((self.x**2) + (self.y**2))**1/2)
    def __neg__(self):
        return Vector2d(self.x*-1, self.y*-1)
    def __add__(self , other):
        return Vector2d((self.x + other.x, other.y))
    def __eq__(self , other):
        return (self.x , self.y) == (other.x , other.y)
    def __sub__(self , other):
        return Vector2d(self.x , other.x) , (self.y , other.y)
   return hypot

