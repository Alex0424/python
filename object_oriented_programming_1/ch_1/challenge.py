# Python Object Oriented Programming by Joe Marini course example
# Programming challenge: define a class to represent a stock symbol

# Challenge: create a class to represent stock information.
# Your class should have properties for:
# Ticker (string)
# Price (float)
# Company (string)
# And a method get_description() which returns a string in the form
# of "Ticker: Company -- $Price"


class Stock:
    ticker: str
    price: float
    company: str

    def __init__(
        self, ticker: str, price: float, company: str
    ) -> None:  # List of arameters
        self.ticker = ticker  # Attribute 1
        self.price = price  # Attribute 2
        self.company = company  # Attribute 3

    def get_description(self):
        return f"{self.ticker}: {self.company} -- ${self.price}"


# ~~~~~~~~~~ TEST CODE ~~~~~~~~~~
msft = Stock("MSFT", 342.0, "Microsoft Corp")
goog = Stock("GOOG", 135.0, "Google Inc")
meta = Stock("META", 275.0, "Meta Platforms Inc")
amzn = Stock("AMZN", 135.0, "Amazon Inc")

print(msft.get_description())
print(goog.get_description())
print(meta.get_description())
print(amzn.get_description())
