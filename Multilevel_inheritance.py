class Car:
    def start(self):
        print("Car Started...")
    def stop(self):
        print("Car Stoped.")

class Toyotacar(Car):
    def __init__(self,brand):
        self.brand = brand
        print(self.brand)

class Fortuner(Toyotacar):
    def __init__(self,type):
        self.type = type
        print(self.type)
        
car1 = Fortuner("Disel")
car1.start()

car2 = Toyotacar("Fortuner")
car2.stop()