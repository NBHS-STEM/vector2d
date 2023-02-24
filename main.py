class Vector2d:
    def __init__ (self x,y):
    self.x=x
    self.y=y
    
    def __repr__ (self):
      return f"Vector2d(x={self.x}, y={self.y})" == True

    def __str__ (self):
      return f"(self.x)+(self.y)"

    def __abs__ (self):
      return f"(self.x**5, self.y**2)"

    def __eq__ (self):
      return f"(self.x==self.y)" == True 

    def __sub__ (self):
      return Vector2d(self.x - other.x, self.y - other.y)
 
    def __add__(self):
      return Vecotr2d(self.x + other.x, self.y + other.y)

    def __neg__(self):
      return Vector2d(-self.x, -self.y)

    def __eq__(self):
      return 