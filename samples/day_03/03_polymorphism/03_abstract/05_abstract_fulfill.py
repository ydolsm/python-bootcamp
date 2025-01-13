from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius

class Polygon(Shape):
    def __init__(self, sides):
        self.sides = sides

    @abstractmethod
    def perimeter(self):
        pass

class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

    def perimeter(self):
        return self.side_length * 4

class Rectangle(Polygon):
    def area(self):
        pass

    def __init__(self, width, height):
        super().__init__(4)
        self.width = width
        self.height = height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)