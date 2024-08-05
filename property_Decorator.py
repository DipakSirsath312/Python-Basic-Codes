# property decorator.
class Student:
    def __init__(self,java,python,php):
        self.java = java
        self.python = python
        self.php = php
        
    @property
    def percentage(self):
        return str((self.java + self.python + self.php) / 3) + "%"

stud1 = Student(39,42,35)
print(stud1.percentage)
stud1.php = 29
print(stud1.percentage)