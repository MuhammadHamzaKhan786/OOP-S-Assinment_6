class Employee:
    def __init__(self, name , salary, ssn):
        self.name = name #public variable
        self._salary = salary #protected variable
        self.__ssn = ssn #private variable

if __name__ == "__main__":
    emp = Employee("Hamza", 60000 , "123-4567-8")  
    #access publlic variable
    print("Public Variable:", emp.name)
    #access protected variable
    print("Protected Variable:", emp._salary)
    #access Private variable
    try:  
       print("Protected Variable:", emp.__ssn)
    except AttributeError:
        print("Cannot access private variabe __ssn")




      