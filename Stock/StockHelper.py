import yfinance as yf
from sys import argv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

from Intersection import Intersection

class StockHelper:
    
    def __init__(self, stock_code: str, period: str):
        stock = yf.Ticker(stock_code.upper())
        # get historical market data
        self.data = stock.history(period=period)
        
        self.data = self.data[self.data.columns.drop(["Dividends", "Stock Splits"])]
        self.data = self.data.set_index(self.data.index.date)
        
        self.DaysAvg = dict()
        self.dayLimit = len(self.data)-20
        
        for n in (3, 5, 7, 10, 20):
            self.DaysAvg[n] = self.getNDaysAverage(n, limit=self.dayLimit)
        
    def plotDaysAverage(self, days_chosen: list[int], intersections:list[Intersection]=None):
        
        for n in days_chosen:
            plt.plot(self.DaysAvg[n], label=f"{n} Days")
        
        if intersections != None:
            for intersection in intersections:
                color = "r" if intersection.up_trend else "b"
                plt.axvline(x=intersection.day, color=color, linestyle='--')
                
        plt.legend()
        plt.show()
        
    def getNDaysAverage(self, n: int, limit: int) -> pd.Series:
        closing_price = self.data["Close"][-(limit+n):][::-1]
        
        temp_sum = closing_price.head(n).sum()
        output_series = pd.Series(dtype=float)
        index = 0
        
        for dt_index, price in closing_price.items():
            if index == limit:
                break
            if index == 0:
                output_series.at[dt_index] = temp_sum / n
            else:
                temp_sum += closing_price[index+n-1] - closing_price[index-1]
                output_series.at[dt_index] = temp_sum / n
            index += 1
        
        return output_series[::-1]
    
    def getLineIntersections(self, target_n: int, remaining_n: list[int], prev_days:int=None) -> list[Intersection]:
        
        prev_days = self.dayLimit if prev_days == None else prev_days
        
        target_line = self.DaysAvg[target_n]
        other_lines = [self.DaysAvg[n] for n in remaining_n]
        
        prev_days = min(prev_days, target_line.size, min([line.size for line in other_lines]))
        
        target_line = target_line[-prev_days:]
        target_prev = target_line[0]
        
        other_prev = list()
        
        for i, line in enumerate(other_lines):
            other_lines[i] = line[-prev_days:]
            other_prev.append(line[0])
            
        intersections = list()
        
        for day_index in range(0, prev_days):
            target_tdy = target_line[day_index]
            for i, line in enumerate(other_lines):
                tdy_target_larger = target_tdy >= line[day_index]
                prev_target_larger = target_prev >= other_prev[i]
                
                if not (tdy_target_larger == prev_target_larger):
                    up_trend = False if tdy_target_larger else True
                    intersections.append(Intersection(
                                n_avg=remaining_n[i],
                                day=line.index[day_index],
                                up_trend=up_trend,
                                targetPercentChange=(target_tdy-target_prev)/target_prev))
                other_prev[i] = line[day_index]
            target_prev = target_tdy
        
        return intersections
    
    def getPriceByDate(self, day: datetime, type="Close") -> float:
        return self.data.loc[pd.to_datetime(day).date()][type]
    
    def getPriceByIndex(self, index=-1, type="Close"):
        """
        Default value is -1, meaning the latest price
        """
        return self.data.iloc[index][type]
        
if __name__ == "__main__":
    try:
        code = argv[1]
    except IndexError:
        code = "TSLA"
    
    try:
        period = argv[2]
    except IndexError:
        period = "12mo"
        
    stock = StockHelper(code, period=period)
    stock.plotDaysAverage([3, 5, 7, 10, 20], stock.getLineIntersections(20, [3,5,7]))