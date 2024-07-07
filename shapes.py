import math


#1 base class shape.
class Shape: 
    def __init__(self, color):
        self._color = color
    def calculate_area(self):
        raise NotImplementedError
    def calculate_perimeter(self):
        raise NotImplementedError
    def get_color(self):
        return self._color
    def set_color(self, color):
        self._color = color

#2 derived class
#circle
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self._radius = radius
    def calculate_area(self):
        return ((math.pi)*(self._radius)**2)
    def calculate_perimeter(self):
        return ((2)*(math.pi)*(self._radius))
#rectangle
class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self._length = length
        self._width = width
    def calculate_area(self):
        return ((self._length)*(self._width))
    def calculate_perimeter(self):
        return ((2)*(self._length + self._width))
#triangle
class Triangle(Shape):
    def __init__(self, color, side1, side2, side3):
        super().__init__(color)
        self._side1 = side1
        self._side2 = side2
        self._side3 = side3
    def calculate_area(self):
        #use Herons formula
        s = (self._side1 + self._side2 + self._side3) / 2
        return math.sqrt(s*(s - self._side1)*(s - self._side2)*(s - self._side3))
    def calculate_perimeter(self):
        return self._side1 + self._side2 + self._side3



