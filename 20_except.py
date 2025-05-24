class InvalidAgeError(Exception):
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be at least 18 to proceed.")
    else:
        print("Age is valid. Access granted!")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except InvalidAgeError as e:
    print("Custom Exception Caught:", e)
except ValueError:
    print("Please enter a valid number.")
