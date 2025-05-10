# Python Object Oriented Programming by Joe Marini course example
# Understanding multiple inheritance


class A:
    def __init__(self):
        super().__init__()
        self.prop1 = "prop1"
        self.title = "Title 1"  # Add


class B:
    def __init__(self):
        super().__init__()
        self.prop2 = "prop2"
        self.title = "Title 2"  # Ignore


class C(A, B):
    def __init__(self):
        super().__init__()


print(C.__mro__)
c = C()
print(c.prop1)
print(c.prop2)
print(c.title)
