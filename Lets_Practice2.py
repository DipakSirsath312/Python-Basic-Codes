class Employee:
    def __init__(self,role,depa,salary):
        self.role = role
        self.depa = depa
        self.salary = salary

    def showDetails(self):
        print("Employee Role:-",self.role)
        print("Employee Deparment:-",self.depa)
        print("Salary:-",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("fresher","IT",15000)
        print("Employee Name:-",self.name)
        print("Age:-",self.age)

Eng1 = Engineer("Ishwar",21)
Eng1.showDetails()