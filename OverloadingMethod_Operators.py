# Overloading Methods And Operators.
class A:
    def __init__(self,a):
        self.a = a

    def __add__(self,o):
        return self.a + o.a

obj1 = A("TYBCA")    
obj2 = A("(ha karle aasan hai bhai)")      
print(obj1 + obj2)