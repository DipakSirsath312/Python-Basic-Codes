class Print_demo():

    def Add(self):
        a = int(input("Ente First Number:-"))
        b = int(input("Ente First Number:-"))
        sum = a + b
        print("Addition=",sum)

    def Sub(self):
        x = int(input("Ente First Number:-"))
        y = int(input("Ente First Number:-"))
        sub = x - y
        print("Subtraction=",sub)

obj1 = Print_demo()
obj1.Add()
obj1.Sub()