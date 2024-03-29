import yfinance as yf

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from RSI import calculateRSI

def trade(code):
    msft = yf.Ticker(code)
    
    # get historical market data
    hist = msft.history(period="24mo")
    hist.reset_index(inplace=True)
    open, close = hist["Open"], hist["Close"]

    principal = 10000
    cash = principal
    bought = False
    bought_price = 0.0
    lot = 0
    
    for i, close_price in close.items():
        if i >= 14:
            close_period = close[i-14:i]
            rsi = calculateRSI(close_period).iloc[-1]
            trade_price = (open[i] + close_price)/2
            if bought:
                if rsi > 70 and bought_price < trade_price:
                    cash += trade_price * lot
                    bought = False
                    bought_price = 0.0
                    lot = 0
            else:
                if rsi < 30:
                    bought = True
                    lot = cash // trade_price
                    bought_price = trade_price
                    cash -= lot * bought_price
    
    print(f"Cash: {cash}")
    print(f"Current Lot: {lot}")
    print(f"Bought Price: {bought_price}")
    print(f"Stock: {lot*close.iloc[-1]}")
    total_asset = cash + lot*close.iloc[-1]
    print(f"Total Asset: {total_asset}")
    gain_loss = (total_asset-principal)/principal*100
    print(f"P/L: {gain_loss}%")
    return gain_loss

if __name__ == "__main__":
    codes = ["RIOT"]
    gain_loss = dict()
    for code in codes:
        gain_loss[code] = trade(code)
    
    print(gain_loss)
    sum = 0
    count = 0
    for k, v in gain_loss.items():
        sum += v
        count += 1
    
    print(f"Average Gain/Loss: {sum/count}")