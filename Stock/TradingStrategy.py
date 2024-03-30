import pandas as pd

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
    
    def sell(self, trade_price: float):
        self.cash += trade_price * self.lot
        self.bought = False
        self.bought_price = 0.0
        self.lot = 0
        
    def buy(self, trade_price: float):
        self.bought = True
        self.lot = self.cash // trade_price
        self.bought_price = trade_price
        self.cash -= self.lot * self.bought_price
                        
    def trade(self, export=False):
        pass
    
    def getPnL(self) -> float:
        return (self.getTotalAsset()-self.principal)/self.principal
    
    def getTotalAsset(self) -> float:
        return self.cash + self.lot*self.stock.getPriceByIndex()
    
    def getStockPnL(self) -> float:
        day1_price = self.stock.getPriceByIndex(0)
        return (self.stock.getPriceByIndex()-day1_price)/abs(day1_price)

    def getEffectiveIncrease(self) -> float:
        stock_return = self.getStockPnL()
        return (self.getPnL() - stock_return)/abs(stock_return)
    
    def printDetails(self) -> None:
        print(f"-------------- Result --------------")
        print(f"{'Stock Code:'.ljust(20,' ')}{self.stock.stock_code}")
        print(f"{'Cash:'.ljust(20,' ')}{self.cash}")
        print(f"{'Current Lot:'.ljust(20,' ')}{self.lot}")
        print(f"{'Bought Price:'.ljust(20, ' ')}{self.bought_price}")
        print(f"{'Stock:'.ljust(20, ' ')}{self.lot*self.stock.getPriceByIndex()}")
        print(f"{'Total Asset:'.ljust(20, ' ')}{self.getTotalAsset()}")
        print(f"{'P/L:'.ljust(20, ' ')}{self.getPnL()*100}%")
        print(f"{'Stock P/L:'.ljust(20, ' ')}{self.getStockPnL()*100}%")
        print(f"{'%Increase by Strat:'.ljust(20, ' ')}{self.getEffectiveIncrease()*100}%")