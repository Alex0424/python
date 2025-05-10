# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass


@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def update_attribute(self, value):
        self.value1 = value


obj = ImmutableClass("Value 30", 938)
print(obj.value1, obj.value2)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Value 387"

# TODO: even functions within the class can't change anything
obj.update_attribute("Value 50")
