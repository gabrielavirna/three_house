""" magic methods 
__mul__ : add __mul__ to NumString so we can multiply our number string by a number."""


class NumString:
    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):  # reflected edition
        return self + other

    def __iadd__(self, other):  # in-place add
        self.value = self + other
        return self.value

    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):  # in-place multiplication
        self.value = self * other
        return self.value


five = NumString(5)
print(5)
print(int(five))
print(float(five))
print("\n")

print(five + 4)
five_3 = NumString(5.3)
print(five_3 + 4)
print(4 + five_3)  # uses __radd__

age = NumString(25)
print(age + 5)
print(5 + age)

age += 1  # uses __iadd__
print(age)

six = NumString(6)
print(six * 2)  # uses __mul__
six_two = NumString(6.2)
print(six_two * 2)

print(2 * six_two)  # uses __rmul__

six *= 2
print(six)
