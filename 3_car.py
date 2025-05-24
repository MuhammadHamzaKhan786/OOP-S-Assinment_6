class Car:
    def __init__(self, brand):
        self._brand = brand


    def start(self):
        print(f"{self._brand} is starting")


my_car = Car("BYD")
print(my_car._brand)
my_car.start()