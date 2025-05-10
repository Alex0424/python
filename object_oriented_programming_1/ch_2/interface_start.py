# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class JSONify(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def JSON_data(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius**2)

    def JSON_data(self):
        return f"{{Apple's half diameter is: {self.radius}}}"


c = Circle(10)
print(c.calcArea())
print(c.JSON_data())
