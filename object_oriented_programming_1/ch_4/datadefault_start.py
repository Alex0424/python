# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field
import random


def price_func():
    return float(random.randrange(20, 40))


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No Title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_func)


b1 = Book(author="Alex")
print(b1)
