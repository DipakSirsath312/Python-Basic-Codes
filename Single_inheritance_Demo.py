class Car:
    car_type = "Disel"
    @staticmethod
    def Start():
        print("Car Started....")
    @staticmethod
    def Stop():
        print("Car Stopped.")

class Toyotacar(Car):
    def __init__(self,name):
        self.name = name
        print(self.name)

car1 = Toyotacar("Fortuner Model")
print(Car.car_type)
car1.Start()
car1.Stop()
print("----------------")
car2 = Toyotacar("Prius Model")
print(Car.car_type)
car2.Start()
car2.Stop()