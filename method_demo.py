class Student:
    def __init__(self,fullname,batch):
        self.fullname = fullname
        self.batch = batch

    def welcome(self):
        print("Welcome Student")
        print(self.fullname)
    
    def get_batch(self):
        return self.batch
    
s1 = Student("Naruto Uzumaki","Junin class")
s1.welcome()
print(s1.get_batch())