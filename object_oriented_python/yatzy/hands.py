"""Now that we can roll dice and compare them, it's time to start on the Yatzy game play."""
from object_oriented_python.yatzy.dice import D6, D20


class Hand(list):
    def __init__(self, size=0, die_class=None, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")
        super().__init__()

        # each time the loop executes, an instance is created
        for _ in range(size):
            self.append(die_class())
        self.sort()


class Hand2(list):
    def __init__(self, size=0, die_class=D20, *args, **kwargs):
        if not die_class:
            raise ValueError("You must provide a die class")

        # each time the loop executes, an instance is created
        for _ in range(size):
            self.append(die_class())

    @property
    def total(self):
        return sum(self)

    @classmethod
    def roll(cls, size):
        return cls(size=size)



class YatzyHand(Hand):
    def __init__(self, *args, **kwargs):
        super().__init__(size=5, die_class=D6, *args, **kwargs)


hand = Hand(size=5, die_class=D6)
print(hand)
print(len(hand))
print(hand[0].value)
print("\n")

yh = YatzyHand()
print(yh)

hand2 = Hand2(size=2)
print(hand2)
t = hand2.roll(2)
print(t.total)

