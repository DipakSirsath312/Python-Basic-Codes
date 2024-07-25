# Encapsulation.
class A:
    _a = 10 # single underscore (protected).
    __b = 20 # double underscore (private).
    def show(self):
        print("a:-",self._a)
        print("b:-",self.__b)

obj1 = A()
obj1.show()
print("outside of class:-",obj1._a) # you can access the outside class and only protected.