# Python Object Oriented Programming by Joe Marini course example
# Basic class definitions


# TODO: create a basic class
class Car:
    def __init__(self, logo, color, price):
        self.logo = logo
        self.color = color
        self.price = price
        self.__secret = "This is an 'easter egg'/'super secret' attribute"

    def getprice(self):
        if hasattr(self, "_amount"):
            return self.price * self._amount
        return self.price

    def setdiscount(self, amount):
        if isinstance(amount, float):
            self._amount = amount
        else:
            print("amount argument must be a float")


# TODO: create instances of the class
car_instance_1 = Car("Volvo", "White", 90000)
car_instance_2 = Car("Audi", "Red", 150000)

# TODO: print the class and property
print(car_instance_1)

print(car_instance_1.logo)
print(car_instance_2.logo)

print(car_instance_1.getprice())
car_instance_1.setdiscount(0.8)
print(car_instance_1.getprice())
print(car_instance_1._Car__secret)
# Internal attribute single underscore('_attribute').
# Apply double underscore('__attribute') when inheritance name clashes are likely.
