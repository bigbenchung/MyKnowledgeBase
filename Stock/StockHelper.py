import yfinance as yf
from sys import argv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

from Intersection import Intersection

class StockHelper:
    
    def __init__(self, stock_code: str, period: str):
        self.stock_code = stock_code
        self.period = period
        
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
        
        fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)

        for n in days_chosen:
            ax1.plot(self.DaysAvg[n], label=f"{n} Days")

        if intersections != None:
            for intersection in intersections:
                color = "r" if intersection.up_trend else "b"
                ax1.axvline(x=intersection.day, color=color, linestyle='--')
        ax1.legend()
        
        ax2.plot(self.data["Close"].iloc[-self.dayLimit:])

        plt.title(self.stock_code)
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
                temp_sum += closing_price.iloc[index+n-1] - closing_price.iloc[index-1]
                output_series.at[dt_index] = temp_sum / n
            index += 1
        
        return output_series[::-1]
    
    def getLineIntersections(self, target_n: int, remaining_n: list[int], prev_days:int=None) -> list[Intersection]:
        
        prev_days = self.dayLimit if prev_days == None else prev_days
        
        target_line = self.DaysAvg[target_n]
        other_lines = [self.DaysAvg[n] for n in remaining_n]
        
        prev_days = min(prev_days, target_line.size, min([line.size for line in other_lines]))
        
        target_line = target_line[-prev_days:]
        target_prev = target_line.iloc[0]
        
        other_prev = list()
        
        for i, line in enumerate(other_lines):
            other_lines[i] = line[-prev_days:]
            other_prev.append(line.iloc[0])
            
        intersections = list()
        
        for day_index in range(0, prev_days):
            target_tdy = target_line.iloc[day_index]
            for i, line in enumerate(other_lines):
                tdy_target_larger = target_tdy >= line.iloc[day_index]
                prev_target_larger = target_prev >= other_prev[i]
                
                if not (tdy_target_larger == prev_target_larger):
                    up_trend = False if tdy_target_larger else True
                    intersections.append(Intersection(
                                n_avg=remaining_n[i],
                                day=line.index[day_index],
                                up_trend=up_trend,
                                targetPercentChange=(target_tdy-target_prev)/abs(target_prev)))
                other_prev[i] = line.iloc[day_index]
            target_prev = target_tdy
        
        return intersections
    
    def getPriceByDate(self, day: datetime, type="Close") -> float:
        return self.data.loc[pd.to_datetime(day).date()][type]
    
    def getPriceByIndex(self, index=-1, type="Close"):
        """
        Default value is -1, meaning the latest price
        """
        return self.data.iloc[index][type]
    
    def getLastTradeDate(self, base_day: datetime) -> datetime:
        datetime_indexer = pd.to_datetime(base_day).date()
        if datetime_indexer == self.data.index[0]:
            print("Cannot find last trade date first row")
            return None

        try:
            base_day_row = self.data.index.get_loc(datetime_indexer)
        except KeyError:
            print("Date not found in index")
            return None
        
        return self.data.index[base_day_row-1]
    
    def getReturn(self, base_day: datetime, lag_days=1) -> float:
        datetime_indexer = pd.to_datetime(base_day).date()
        
        if datetime_indexer == self.data.index[0]:
            print("Cannot generate return for first row")
            return None
        
        try:
            base_day_row = self.data.index.get_loc(datetime_indexer)
        except KeyError:
            print("Date not found in index")
            return None
        
        if base_day_row - lag_days < 0:
            print("The dataset does not contain enough data to calculate this lag return")
            return None
        
        lagged_price = self.data.iloc[base_day_row - lag_days]
        return (self.data.iloc[base_day_row]["Close"] - lagged_price["Close"]) / abs(lagged_price["Close"])
    
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