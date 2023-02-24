import math
class Vector2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f"Vector2d(x={self.x}, y={self.y})"
    def __str__(self):
        return f"{self.x}i + {self.y}j"
    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)
    def __neg__(self):
        self.x *= -1
        self.y *= -1
        return f"Vector2d({self.x}, {self.y})"
    def __add__(self, other):
        apple = self.x + other.x
        banana = self.y + other.y
        return f"Vector2d({apple}, {banana})"
    def __eq__(self, other):
        if self.x == other.x:
            if self.y == other.y:
                return True
        else:
            return False
    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return f"Vector2d({x}, {y})"
    def angle(self):
        return  math.degrees(math.atan2(self.y, self.x))