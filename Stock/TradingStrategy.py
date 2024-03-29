from StockHelper import StockHelper

class TradingStrategy:
    """
    Parent class
    """
    def __init__(self, stock: StockHelper, principal: float):
        self.stock = stock
        self.principal = principal
        self.cash = principal
        self.bought = False
        self.bought_price = 0.0
        self.lot = 0
    
    def trade(self):
        pass
    
    def getPnL(self) -> float:
        return (self.getTotalAsset()-self.principal)/self.principal
    
    def getTotalAsset(self) -> float:
        return self.cash + self.lot*self.stock.getPriceByIndex()
    
    def printDetails(self) -> None:
        print(f"Cash: {self.cash}")
        print(f"Current Lot: {self.lot}")
        print(f"Bought Price: {self.bought_price}")
        print(f"Stock: {self.lot*self.stock.getPriceByIndex()}")
        print(f"Total Asset: {self.getTotalAsset()}")
        print(f"P/L: {self.getPnL()*100}%")
    