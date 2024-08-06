class A:
    def __init__(self,a):
        self.a = a
    
    def __lt__(self,other):
        if(self.a < other.a):
            return "obj1 is lessthan obj2"
        else:
            return "obj2 is lessthan obj1"
        
    def __gt__(self,other):
        if(self.a > other.a):
            return "obj1 is greater than obj2"
        else:
            return "obj2 is greater than obj1"
        
    def __eq__(self,other):
        if(self.a == other.a):
            return "Both are Equal"
        else:
            return "Not Equal"
        
obj1 = A(65)
obj2 = A(76)
print(obj1 < obj2)

obj1 = A(45)
obj2 = A(55)
print(obj1 > obj2)

obj1 = A(2)
obj2 = A(2)
print(obj1 == obj2)