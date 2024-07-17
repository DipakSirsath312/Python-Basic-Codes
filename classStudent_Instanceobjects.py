class Student:
    stucount = 0

    def __init__(self,name,subject,fees):
        self.name = name
        self.subject = subject
        self.fees = fees
        Student.stucount += 1

    def displayCount(self):
        print("Total Students:-",Student.stucount)

    def displayStudent(self):
        print("Name:-",self.name,"Subject:-",self.subject,"College_Fees:-",self.fees)

stud1 = Student("Yogesh,","Java,",20000)
stud2 = Student("Ishwar,","C++,",21000)

stud1.displayCount()
stud1.displayStudent()
stud2.displayStudent()