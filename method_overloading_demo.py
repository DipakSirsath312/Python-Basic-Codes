# Method Overloading.
class Employee:
    def Emp_hello(self,emp_name = None):
        if emp_name is not None:
            print("Hello",emp_name)
        else:
            print("Hello")

emp1 = Employee()
emp1.Emp_hello()
emp1.Emp_hello("World")