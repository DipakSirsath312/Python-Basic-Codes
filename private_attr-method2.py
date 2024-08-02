class Person:
    __name = "Dipak" # private attribute.

    def __hello(self): # private method.
        print("Welcome Person!")

    def call(self):
        self.__hello()
        print(self.__name)

per1 = Person()
per1.call()