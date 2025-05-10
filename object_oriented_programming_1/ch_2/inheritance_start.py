# Python Object Oriented Programming by Joe Marini course example
# Understanding class inheritance


class BookParent:
    def __init__(self, price, title):
        self.price = price
        self.title = title


class AnotherParent:
    def __init__(self, price, title, publisher, period):
        self.price = price
        self.title = title
        self.period = period
        self.publisher = publisher


class Book(BookParent):
    def __init__(self, title, author, pages, price):
        self.author = author
        self.pages = pages
        super().__init__(price, title)


class Magazine(AnotherParent):
    def __init__(self, title, publisher, price, period):
        super().__init__(price, title, publisher, period)


class Newspaper(AnotherParent):
    def __init__(self, title, publisher, price, period):
        super().__init__(price, title, publisher, period)


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")

print(b1.author)
print(n1.publisher)
print(b1.price, m1.price, n1.price)
