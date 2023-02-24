import math 
class Vector2d:
    def _init_(self, x, y):
         self.x =x
         self.y =y
   
    def _repr_(self):
        return f"Vecto2d(x={self.x}, y={self.y}) is True"
    
    def _str_(self):
        return f"{self.x}i, {self.y}j"
    
    def _abs_(self):
        hypotenuse = (self.x**2+self.y**2)**.5
        return hypotenuse
   def _neg_(self)
       return Vector2d(self.x*-1, self.y*-1)
    def __eq__(self):
        if Vector2d((self.x, self.y)==(other.x,other.y))
              return True
    
    def_sub_(self):
        if vector2d((self.x-other.y), (self.x-other.y))

    def_angle_(self):
        return math.degress(math.atan2(self.y,self.x))
          