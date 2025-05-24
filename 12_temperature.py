class TemperatureConverter():

    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
if __name__ == "__main__":  
    print("Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(0))
    print("Fahrenheit:", TemperatureConverter.celsius_to_fahrenheit(200))  