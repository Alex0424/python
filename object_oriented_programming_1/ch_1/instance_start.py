# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.price = price
        self.__secret = "Secret"

    # TODO: create instance methods
    def changeauthor(self, new_author):
        self.author = new_author

    def newprice(self, new_price):
        self.price = new_price

    def discount(self, amount: float):
        if 1 >= amount >= 0:
            self.price = self.price * amount
        else:
            raise ValueError("Error, only accepts number between 1 and 0")


# TODO: create some book instances
b1 = Book("War and Peace", "Tolstoy", 600.99)
b2 = Book("The Catcher in the Rye", "Salinger", 399.99)

# TODO: print the price of book1
print(b1.price)

# TODO: try setting the discount
b1.discount(0.1)
print(b1.price)

# TODO: properties with double underscores are hidden by the interpreter
