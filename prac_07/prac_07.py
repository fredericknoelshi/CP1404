class Point:
    def __init__(self, a=0.0, b=0.0):
        self.a = a
        self.b = b

    def __add__(self, other):  # Magic method
        return Point(self.a + other.a, self.b + other.b)  # For Addition

    def __sub__(self, other):
        return Point(self.a - other.a, self.b - other.b)  # For Subtraction

    def __mul__(self, other):
        return Point(self.a * other.a, self.b * other.b)  # For Multiplication

    def __truediv__(self, other):
        return Point(self.a / other.a, self.b / other.b)  # For Division

    def __pow__(self, power):
        return Point(self.a ** power)  # For Power

    def __floordiv__(self, other):
        return Point(self.a // other.a, self.b // other.b)  # For //

    def __lt__(self, other):
        return self.a < other.a and self.b < other.b  # For Less than

    def __le__(self, other):
        return self.a <= other.a and self.b <= other.b  # For Less than or equal to

    def __gt__(self, other):
        return self.a > other.a and self.b > other.b  # For Greater than

    def __ge__(self, other):
        return self.a >= other.a and self.b >= other.b  # For Greater than or equal to

    def __eq__(self, other):
        return self.a == other.a  # For Comparing values


here = Point(4.5, 6.7)
there = Point(6.7, 5.9)
print(here + there)  # Doesn't work so need magic method
