import math
class Vector2d:
  def __init__(self,x,y):
    self.x=x
    self.y=y
  def __repr__(self):
    return f"Vector2d(x={self.x}, y={self.y})"
  def __str__(self):
    return f"{self.x}i:{self.y}j"
  def __abs__(self):
    leg1=self.x**2
    leg2=self.y**2
    legs=leg1+leg2
    return math.sqrt(legs)
  def __neg__(self):
    return Vector2d(self.x*-1,self.y*-1)
  def __add__(self,other):
    return Vector2d((self.x + other.x),(self.y + other.y))