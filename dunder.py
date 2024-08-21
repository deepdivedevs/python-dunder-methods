class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
        
    def __str__(self):
        return f"Point({self.x}, {self.y})"
    
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False
    
    def __getitem__(self, key):
        if key == 0:
            return f"x: {self.x}"
        if key == 1:
            return f"y: {self.y}"
        else:
            raise IndexError(f"key: {key} out of range")