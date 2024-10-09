from math import pi


class Shape:

    def calculate_area(self):
        return 0

    def __add__(self, other):
        return self.calculate_area() + other.calculate_area()


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius


    def calculate_area(self):
        return pi * self.radius ** 2


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

class Triangle(Shape):

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height
