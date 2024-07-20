class Student:
    colleage_name = "Imrd Colleage Shahada" # class attr.

    def __init__(self,name,marks):
        print("Adding New Student in Database")
        self.name = name 
        self.marks = marks
    
print(Student.colleage_name)
s1 = Student("Madara",99.9)                  # object attr.
print("Name:-",s1.name,"Marks:-",s1.marks)

s2 = Student("itachi",99)
print("Name:-",s2.name,"Marks:-",s2.marks)