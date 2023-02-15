class Vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y 

    def __reper__(self):
        return f"Vector 2D(x = {self.x},y-{self.y}"
        
    def __str__(self):
        return f"Vector 2D({self.x}i + {self.y}j"

    def __abs__(self):
        lenght = self.x**2 + self.y**2 
      return lenght ** (1/2)

