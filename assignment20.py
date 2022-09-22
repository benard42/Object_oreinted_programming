class Family:
    
    def __init__(self,name,location,number):
        self.name = name
        self.location = location
        self.number = number
    
    def __repr__(self):
        return f"<Family {self.name} {self.location} {self.number}>"


class Nyeyembe(Family):
    def __init__(self):
        return f"<Family {self.name} {self.location} {self.number}>"
        # super().__init__()

#polymorphsm

class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def work(self):
        return 'Employee work'
    
class Mother(Family):
    
    def work(self):
        return 'Mother works for the family'
    
class Father(Family):
    def work(self):
        return 'Father works for the family'


#Encapsulation
class Family:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.Earnings = 100
        
        
    def earn(self):
        return '{} earns {}.'.format(self.name, self.Earnings)
   
    def setSalary(self, Earnings):
        self.Earnings = Earnings

fam = Family("benard","Kyamuhunga","0777635")