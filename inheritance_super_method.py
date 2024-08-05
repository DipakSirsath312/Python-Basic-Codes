# super method.
class Car:
    def __init__(self,type):
        self.type = type

    def start(self):
        print("Car Started...")

    def stop(self):
        print("Car Stoped.")

class Toyotacar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()
        
car1 = Toyotacar("Prius","Eletricals")
print(car1.name)
print(car1.type)
car1.stop()