"""Add a new property to the Rectangle class named area. 
It should calculate and return the area of the Rectangle  instance (width * length).
Let's add one more property to our Rectangle class. This time, add a perimeter 
property that returns the perimeter  of the rectangle (length * 2 + width * 2).
"""


class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    @property
    def area(self):
        return self.width * self.length

    @property
    def perimeter(self):
        return self.length*2 + self.width*2

rec = Rectangle(10, 5)
print(rec.area)
print(rec.perimeter)