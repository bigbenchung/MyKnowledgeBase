from sys import argv

from RSI import calculateRSI
from StockHelper import StockHelper
from TradingStrategy import TradingStrategy

class RSITrading(TradingStrategy):
    
    def __init__(self, stock: StockHelper, principal: float):
        super().__init__(stock, principal)
    
    def trade(self):
        hist = self.stock.data.reset_index()
        open, close = hist["Open"], hist["Close"]
        
        for i, close_price in close.items():
            if i >= 14:
                close_period = close[i-14:i]
                rsi = calculateRSI(close_period).iloc[-1]
                trade_price = (open[i] + close_price)/2
                if self.bought:
                    if rsi > 70 and self.bought_price < trade_price:
                        self.cash += trade_price * self.lot
                        self.bought = False
                        self.bought_price = 0.0
                        self.lot = 0
                else:
                    if rsi < 30:
                        self.bought = True
                        self.lot = self.cash // trade_price
                        self.bought_price = trade_price
                        self.cash -= self.lot * self.bought_price

if __name__ == "__main__":
    try:
        code = argv[1]
    except IndexError:
        code = "TSLA"
    
    try:
        principal = argv[2]
    except IndexError:
        principal = 10000
    
    trading = RSITrading(
        stock=StockHelper(stock_code=code, period="24mo"), 
        principal=principal
    )
    trading.trade()
    trading.printDetails()