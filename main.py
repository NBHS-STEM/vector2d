import math
class Vector2d: 
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Vector2d(x = {self.x}, y = {self.y})"
    def __str__(self):
            return f"{self.x}i + {self.y}j"
    def __abs__(self):
            return ((self.x**2)+(self.y**2))**(1/2)
    def __neg__(self):
          return f"Vector2d(-{self.x},-{self.y})"
    def __add__(self,other):
        sum_x = self.x + other.x
        sum_y = self.y + other.y
        return f"Vector2d({sum_x},{sum_y})"
    def __eq__(self,other):
        return (self.x ,self.y)== (other.x,other.y)
    def __sub__(self,other):
        diff_x = self.x - self.x
        diff_y = self.y - self.y
        return f"Vector2d({diff_x},{diff_y})"
    def angle(self):
         tan = math.atan2(self.x),(self.y)
         return math.degrees(tan)
         


    
    
         