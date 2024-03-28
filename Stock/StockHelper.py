import yfinance as yf
from sys import argv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from Intersection import Intersection

class StockHelper:
    
    def __init__(self, data: pd.DataFrame):
        self.data = data[data.columns.drop(["Dividends", "Stock Splits"])]
        self.data = self.data.set_index(self.data.index.date)
        self.DaysAvg = dict()
        for n in (3, 5, 7, 10, 20):
            self.DaysAvg[n] = self.getNDaysAverage(n)
        
        self.plotDaysAverage([3, 5, 7, 10, 20], self.getLineIntersections(20, [3,5,7]))
        
    def plotDaysAverage(self, days_chosen: list[int], intersections:list[Intersection]=None):
        
        for n in days_chosen:
            plt.plot(self.DaysAvg[n], label=f"{n} Days")
        
        if intersections != None:
            for intersection in intersections:
                color = "r" if intersection.up_trend else "b"
                plt.axvline(x=intersection.day, color=color, linestyle='--')
                
        plt.legend()
        plt.show()
        
    def getNDaysAverage(self, n: int, limit=60) -> pd.Series:
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
        
        return output_series
    
    def getLineIntersections(self, target_n: int, remaining_n: list[int], limit=60) -> list[Intersection]:
        
        target_line = self.DaysAvg[target_n]
        other_lines = [self.DaysAvg[n] for n in remaining_n]
        other_prev = list()
        other_sizes = list()
        target_prev = target_line[-1]
        
        for line in other_lines:
            other_prev.append(line[-1])
            other_sizes.append(line.size)
            
        limit = min(limit, target_line.size, min(other_sizes))
        
        del other_sizes
        
        intersections = list()
        
        for day_index in range(limit-2, -1, -1):
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
        
if __name__ == "__main__":
    try:
        code = argv[1]
    except IndexError:
        code = "TSLA"
    
    code = code.upper()
    
    stock = yf.Ticker(code)
    # get historical market data
    hist = stock.history(period="12mo")
    
    stock = print(StockHelper(hist))