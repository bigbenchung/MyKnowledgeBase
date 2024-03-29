from sys import argv
from datetime import datetime

from StockHelper import StockHelper
from TradingStrategy import TradingStrategy
from Intersection import Intersection

class GoldenCrossTrading(TradingStrategy):
    
    def __init__(self, stock: StockHelper, principal: float, target_n: int, remaining_n: list[int]):
        super().__init__(stock, principal)
        self.target_n = target_n
        self.remaining_n = remaining_n
        self.default = dict()
        
        for n in remaining_n:
            self.default[n] = False
    
    def resetCheck(self) -> dict:
        return self.default
        
    def trade(self):
        
        self.intersections: list[Intersection] = self.stock.getLineIntersections(target_n=20, remaining_n=[3,5,7])
        check = self.resetCheck()
        up_trend = None
        
        for intersection in self.intersections:
            if up_trend == None:
                up_trend = intersection.up_trend
            
            if intersection.up_trend == up_trend:
                check[intersection.n_avg] = True
                if set(check.values()) == {True}:
                    trade_price = self.stock.getPriceByDate(intersection.day, "Open")
                    if up_trend and not self.bought:
                        print(f"Buy at {round(trade_price, 2)} on {intersection.day}")
                        self.buy(trade_price)
                        check = self.resetCheck()
                    elif not up_trend and self.bought:
                        print(f"Sell at {round(trade_price,2)} on {intersection.day}")
                        self.sell(trade_price)
                        check = self.resetCheck()
            else:
                up_trend = not up_trend
                check = self.resetCheck()

if __name__ == "__main__":
    try:
        code = argv[1]
    except IndexError:
        code = "TSLA"
    
    try:
        principal = argv[2]
    except IndexError:
        principal = 10000
    
    trading = GoldenCrossTrading(
        stock=StockHelper(stock_code=code, period="24mo"), 
        principal=principal,
        target_n=20,
        remaining_n=[3,5,7]
    )
    trading.trade()
    trading.printDetails()