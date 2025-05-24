class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, number):
        return number * self.factor
    
double = Multiplier(2)
triple = Multiplier(3)


print(callable(double))  


print(double(10))  
print(triple(5))  
