# Let's Practice Methods.
class Student:
    Colleage_name = "Imrd Colleage Shahada"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",self.name,"your avg score is:-", sum/3)

print(Student.Colleage_name) 
s1 = Student("Shinchan Noharas",[74,85,79])
s1.get_avg()
s1.name = "Tony Stark"
s1.marks = [70,89,90]
s1.get_avg()

s2 = Student("Chetan patil",[87,72,81])
s2.get_avg()
s2.name = "Ishwar Bachhav"
s2.marks = [86,79,70]
s2.get_avg()