class Person:
    def __init__(self,name):
        self.name = name
        
class Employee(Person):
    def __init__(self,name, salary):
        super().__init__(name)
        self.salary = salary

    def get_data(self):
        return self.name, self.salary