class Person:
    name = "anonymous"
    @classmethod
    def changename(cls,name):
        cls.name = name

p1 = Person()
p1.changename("Shubham")
print(p1.name)
print(Person.name)