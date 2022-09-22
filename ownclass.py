class Company:
    def __init__(self,Name, Location, Number_of_Employees, Company_TIN,Kind_of_company):
        self.Name = Name
        self.Location = Location
        self.Number_of_Employees = Number_of_Employees
        self.Company_TIN = Company_TIN
        self.Kind_of_company = Kind_of_company

def __repr__(self):
    return f"<company {self.Name} {self.Location} {self.Number_of_Employees} {self.Company_TIN} {self.Kind_of_company}>"
        
NITA = Company("NITA-U","Lugogo",120,101982873,"Governmet")
WIMEA = Company("WIMEA","Makerere",20,20198273,"Private")

print("your company is " + NITA.Name + " located at " + NITA.Location)
print(NITA.Location)
print(NITA.Number_of_Employees)
print(NITA.Company_TIN)
print(NITA.Kind_of_company)


print(WIMEA.Name)
print(WIMEA.Location)
print(WIMEA.Number_of_Employees)
print(WIMEA.Company_TIN)
print(WIMEA.Kind_of_company)


