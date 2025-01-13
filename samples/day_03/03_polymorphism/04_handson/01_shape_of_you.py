from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Polygon(Shape, ABC):
    def __init__(self, sides):
        self.sides = sides

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Polygon):
    pass

class Triangle(Polygon):
    pass

class Square(Rectangle):
    pass

class Circle(Shape):
    pass
