import random


class Dice:
    def __init__(self, sides=2, value=0):
        if not sides >= 2:
            raise ValueError("Must have at least 2 sides")
        if not isinstance(sides, int):
            raise ValueError("Sides must be a whole number")

        if not isinstance(value, int):
            raise ValueError("Value must be an int")

        self.value = value or random.randint(1, sides)

    def __int__(self):
        return int(self.value)

    def __eq__(self, other):
        return int(self) == other

    def __ne__(self, other):
        return int(self) != other

    def __gt__(self, other):
        return int(self) > other

    def __lt__(self, other):
        return int(self) < other

    def __ge__(self, other):
        return int(self) > other or int(self) == other

    def __le__(self, other):
        return int(self) < other or int(self) == other

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other

    def __repr__(self):
        return str(self.value)


class Die:
    def __init__(self, sides=2):
        if sides < 2:
            raise ValueError("Can't have fewer than 2 sides")
        self.sides = sides
        self.value = random.randint(1, sides)

    def __int__(self):
        return self.value

    def __add__(self, other):
        return int(self) + other

    def __radd__(self, other):
        return int(self) + other


class D6(Dice):
    def __init__(self, value=0):
        super().__init__(sides=6, value=value)


class D20(Die):
    def __init__(self):
        super().__init__(sides=20)


d = Dice()
print(d.value)
d6 = Dice(sides=6)
print(d6.value)
d6 = D6()
print(d6.value)
print("\n")

d1 = D6()
print(d1 < 2, d1 <= 2, d1 > 1, d1 != 4, d1 == 6)
d2 = D6()
print(d1 + d2)
print("\n")

d20 = D20()
print(d20.sides, d20.value)