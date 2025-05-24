class Engine:
    def start(self):
        print("Engine has started.")
        

class Car:
    def __init__(self):
        self.engine = Engine() #composition

    def start_car(self):
        self.engine.start()

if __name__ == "__main__":
    my_car = Car()
    my_car.start_car()
