class Student:
    def __init__(self,name):
        self.name = name

s1 = Student("Dipak")
del s1.name # delete Attribute.
print(s1.name)

del s1  # delete object.
print(s1)