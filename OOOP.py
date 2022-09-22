#Inheritance
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Manager(Employee):
    def __init__(self.name):
        super().__init__()
    def supervise(self):
        return '{} is supervising'.format(self.name)
    
class Boss(Employee):
    #add new method
    def fire(self):
        return '{} is firing employee'.format(self.name)


#Encapsulation

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__salary = 100
        
    def earn(self):
        return '{} earns {}.'.format(self.name, self.__salary)
   
    def setSalary(self, salary):
        self.__salary = salary

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self):
        return 'Employee work'

#polymorphsm


class Manager(Employee):
    #polymorphsm
    def work(self):
        return 'Manager work'
    
class Boss(Employee):
    #polymorphsm
    def work(self):
        return 'Boss work'