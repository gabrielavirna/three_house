import random


class Character:
    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky

    def pickpocket(self):  # self = instance that is using the method
        return self.sneaky and bool(random.randint(0, 1))

    def hide(self, light_level):
        return self.sneaky and light_level < 10


kenneth = Thief("Kenneth", sneaky=False, clever=True)
print(kenneth.name)
print(kenneth.sneaky)
kenneth.sneaky = True
print(kenneth.sneaky)
print("\n")

gabriela = Thief("Gabriela", scars=None, fav_weapon="Wit")
print(gabriela.name)
print(gabriela.sneaky)
print(gabriela.fav_weapon)
