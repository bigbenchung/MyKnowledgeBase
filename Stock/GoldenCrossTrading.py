from sys import argv
from datetime import datetime

import numpy as np
import pandas as pd
from pickle import dumps, loads

from StockHelper import StockHelper
from TradingStrategy import TradingStrategy
from Intersection import Intersection

class GoldenCrossTrading(TradingStrategy):
    
    def __init__(self, stock: StockHelper, principal: float, target_n: int, remaining_n: list[int]):
        super().__init__(stock, principal)
        self.target_n = target_n
        self.remaining_n = remaining_n
        default = dict()
        
        for n in remaining_n:
            default[n] = False
        self.default = dumps(default)
        
    def resetCheck(self) -> dict:
        return loads(self.default)
    
    def getBuySellSignals(self, intersections: list[Intersection]) -> list[dict]:
        # containing dict with keys date, buy/sell, trade_price, intersection
        signals = list()
        check = self.resetCheck()
        up_trend = None

        for i, intersection in enumerate(intersections):
            if up_trend == None:
                up_trend = intersection.up_trend
            
            if intersection.up_trend != up_trend:
                up_trend = not up_trend
                check = self.resetCheck()
                
            if intersection.up_trend == up_trend:
                check[intersection.n_avg] = True
                if set(check.values()) == {True}:
                    trade_price = self.stock.getPriceByDate(intersection.day, "Open")
                    if up_trend and (not signals or signals[-1]["buy/sell"] == "sell"):
                        signals.append({"date": intersection.day, 
                                        "buy/sell": "buy", 
                                        "trade_price": trade_price,
                                        "intersection": intersection})
                        check = self.resetCheck()
                    elif not up_trend and signals:
                        if signals[-1]["buy/sell"] == "buy":
                            signals.append({"date": intersection.day, 
                                            "buy/sell": "sell", 
                                            "trade_price": trade_price,
                                            "intersection": intersection})
                            check = self.resetCheck()

        return signals

    def trade(self, export=False):

        if export:
            export_df = pd.DataFrame(columns=["buy_lag1_return", "buy_20day_slope", "gain/loss"])
            index_tracker = 0
            
        intersections: list[Intersection] = self.stock.getLineIntersections(target_n=self.target_n, remaining_n=self.remaining_n)
        
        signals = self.getBuySellSignals(intersections)
        
        for signal in signals:
            # check for buy signal
            if not self.bought:
                if signal["buy/sell"] == "buy":
                    self.buy(signal["trade_price"])
                    if export:
                        intersection: Intersection = signal["intersection"]
                        ref_day = self.stock.getLastTradeDate(intersection.day)
                        new_row = [self.stock.getReturn(ref_day, 1), intersection.targetPercentChange, signal["trade_price"]]
            # check for sell signal
            else:
                if signal["buy/sell"] == "sell":
                    self.sell(signal["trade_price"])
                    if export:
                        if new_row:
                            new_row[-1] = (signal["trade_price"] - new_row[-1]) / abs(new_row[-1])
                            export_df.loc[index_tracker] = new_row
                            index_tracker += 1
                            del new_row

        if export:
            return export_df
            
if __name__ == "__main__":
    try:
        code = argv[1]
    except IndexError:
        code = "TSLA"
    
    try:
        principal = argv[2]
    except IndexError:
        principal = 10000
    
    try:
        period = argv[3]
    except IndexError:
        period = "24mo"
        
    trading = GoldenCrossTrading(
        stock=StockHelper(stock_code=code, period=period), 
        principal=principal,
        target_n=20,
        remaining_n=[3,5,7]
    )
    trading.trade()
    trading.printDetails()
    
    for i in StockHelper(stock_code=code, period=period).getLineIntersections(20, [3,5,7]):
        print(i.day, i.up_trend, i.n_avg)