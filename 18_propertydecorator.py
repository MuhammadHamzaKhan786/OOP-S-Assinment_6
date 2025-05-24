class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        print(f"Setting price to {value}...")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(500)

print(p.price)

p.price = 1000 

print(p.price) 
