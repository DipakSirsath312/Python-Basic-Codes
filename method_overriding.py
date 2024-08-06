# method overriding.
class Test1:
    def add(self,a,b):
        print("Sum of Two:-",a + b)

class Test2(Test1):
    def add(self,a,b,c):
        print("Sum of Three:-",a + b + c)

tst1 = Test1()
tst1.add(15,25)
print("--------------------")
tst2 = Test2()
tst2.add(15,25,60)