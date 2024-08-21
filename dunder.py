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

# See list of dunder methods here: https://docs.python.org/3/reference/datamodel.html
a = Point(1, 2)
b = Point(3, 4)

# __str__ called
print(a)

# __add__ called
print(a + b)

# __sub__ called
print(a - b)

# __mul__ called
print(a * b)

# __eq__ called
print(a == b)

# __getitem__ called
print(a[0])
