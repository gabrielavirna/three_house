""""Emulating Built-ins"""

from object_oriented_python.multiple_superclasses.items import Item, Weapon


class Inventory:
    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        # for item in self.slots:
        #     yield item
        yield from self.slots

coin = Item('coin', 'a gold coin')
inventory = Inventory()
inventory.add(coin)
print(len(inventory))

sword = Item('sword', 'sharp')
inventory.add(sword)
print(sword in inventory)

sword2 = Weapon('sword', 'sharp', '50')
inventory2 = Inventory()
inventory2.add(sword2)
for item in inventory2:
    print(item.description)