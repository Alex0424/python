# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
print(type(b1))
print(type(n1))

# TODO: compare two types together
if type(b1) is Newspaper:
    print(f"{b2.title} is same class type")
else:
    print(f"{b1.title} is not same class type")


# TODO: use isinstance to compare a specific instance to a known type
print(f"Is {b1.title} a Newspaper class type?: ", isinstance(b1, Newspaper))
print(f"Is {b1.title} a Book class type?: ", isinstance(b1, Book))
