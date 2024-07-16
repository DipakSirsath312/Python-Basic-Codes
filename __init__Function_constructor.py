class Student:
    # parameterized constructors.
    def __init__(self,fullname):
        self.name = fullname

s1 = Student("Madara Uchiha")
print(s1.name)

s2 = Student("Itachi Uchiha")
print(s2.name)