"""We need to be able to set the price of a product through a property setter.
Add a new setter (@price.setter) method to the Product class that updates the _price attribute."""


class Product:
    _price = 0.0
    tax_rate = 0.12

    def __init__(self, base_price):
        self.price = base_price

    @property
    def price(self):
        return self._price + (self._price * self.tax_rate)

    @price.setter
    def price(self, price):
        self._price = price 

p = Product(11)
print(p.price)
