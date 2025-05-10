# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCODED", "PAPERBACK", "EBOOK")
    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def get_book_type(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist

    def get_name(self):
        return self.title

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def set_title(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if booktype in Book.BOOK_TYPES:
            self.booktype = booktype
        else:
            raise ValueError(f"{booktype} is not a valid book type!")


# TODO: access the class attribute
print("Book types: ", Book.get_book_type())

# TODO: Create some book instances
b1 = Book("Megalodon", "HARDCODED")
b2 = Book("Harry Potter", "EBOOK")
print(b1.booktype)

# TODO: Use the static method to access a singleton object

books = Book.getbooklist()
print(books)
books.append(b1.title)
books.append(b2.title)
books = Book.getbooklist()
print(books)

print(b2.get_name())
