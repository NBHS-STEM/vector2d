class Vector2d:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Vector2d(x={self.x},y={self.y})'
    
    def __str__(self):
        return f'{str(self.x)}i + {str(self.y)}j'
    
    def __abs__(self):
        return ((self.x)**2 + (self.y)**2)**(1/2)
    
    def __neg__(self):
        return f'Vector2d({self.x * (-1)},{self.y * (-1)})'
    
    def __add__(self,other):
        return f'Vector2d({self.x+other.x},{self.y+other.y})'
    
    def __eq__(self,other):
        return self.x == other.x and self.y == self.y

    def __sub__(self,other):
        return f'Vector2d({self.x-other.x},{self.y-other.y})'