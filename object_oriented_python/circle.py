
class Circle:
    def __init__(self, diameter):
        self.diameter = diameter

    # proprieties act like attributes, but cannot be set without the setter
    @property
    def radius(self):
        return self.diameter / 2

    @radius.setter  # name the getter and setter methods the same
    def radius(self, radius):
        self.diameter = radius * 2


small = Circle(10)
print(small.diameter)
print(small.radius)

