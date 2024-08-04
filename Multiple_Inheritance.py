class A:
    def show(self):
        print("Welcome Class A")

class B:
    def print(self):
        print("Welcome Class B")

class C(A,B):
   def out(self):
       print("Welcome Class C")

stud = C()
stud.show()
stud.print()
stud.out()