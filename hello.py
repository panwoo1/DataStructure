import math

class Point:
    def __init__ (self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __rmul__(self, other):
        return Point(self.x * other, self.y * other)

    def length(self):
        return math.sqrt(self.x**2 + self.y**2)

    def dot(self, q):
        return self.x*q.x + self.y*q.y

    def dist(self, q):
        return (self - q).length()

    def move(self, dx = 0, dy = 0):
        self.x += dx
        self.y += dy

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def get(self):
        return Point(self.x, self.y)

    def setX(self, x = 0):
        self.x = x

    def setY(self, y = 0):
        self.y = y

    def set(self, x = 0, y = 0):
        self.x = x
        self.y = y

p = Point(1, 2)
q = Point(2, 3)
print(f"p = {p}, q = {q}")
print("length of p =", p.length())
print("dot of p and q =", p.dot(q))
print("dist of p and q =", p.dist(q))
p.move(3, 5)
print("move p by (3, 5) =", p)