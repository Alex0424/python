from abc import ABC, abstractmethod


class Asset(ABC):
    def __init__(self, price):
        self.price = price

    @abstractmethod
    def get_description():
        pass


class Stock(Asset):
    sticker: str
    price: float
    description: str

    def __init__(self, ticker, price, description):
        self.ticker = ticker
        self.description = description
        super().__init__(price)

    def get_description(self):
        return f"{self.ticker}: {self.description} -- ${self.price}"


class Bond(Asset):
    bondprice: float
    bondname: str
    duration: int
    intrest: float

    def __init__(self, bondprice, bondname, duration, intrest):
        self.bondprice = bondprice
        self.bondname = bondname
        self.duration = duration
        self.intrest = intrest

    def get_description(self):
        return f"{self.bondname}: {self.duration} : ${self.bondprice} : {self.intrest}%"


ticker = "MSFT"
price = 400.00
description = "Microsoft Corporation"
bondname = "30 Year US Treasury"
bondprice = 100.00
duration = 30
interest = 4.38

stock = Stock(ticker, price, description)
print(stock.get_description())

bond = Bond(bondprice, bondname, duration, interest)
print(bond.get_description())
