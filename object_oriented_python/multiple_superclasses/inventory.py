""" Override the add_item method. Use super() in it to make sure the item still gets added to the list. 
Use the list.sort() method to make sure the slots list gets sorted after an item is added. Only do this in the 
SortedInventory class."""


class Inventory:
    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)


class SortedInventory(Inventory):
    def add_item(self, item):
        super().add_item(item)
        list.sort(self.slots)

    def __repr__(self):
        return "Slots are: {}".format(self.slots)


si = SortedInventory()
si.add_item(12)
si.add_item(11)
si.add_item(13)
print(si)