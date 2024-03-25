import yfinance as yf
from typing import Callable
from sys import argv

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def calculateRSI(over: pd.Series, fn_roll: Callable = lambda s: s.ewm(span=14).mean()) -> pd.Series:
    
    length = 14
    # Get the difference in price from previous step
    delta = over.diff()
    # Get rid of the first row, which is NaN since it did not have a previous row to calculate the differences
    delta = delta[1:] 

    # Make the positive gains (up) and negative gains (down) Series
    up, down = delta.clip(lower=0), delta.clip(upper=0).abs()

    roll_up, roll_down = fn_roll(up), fn_roll(down)
    rs = roll_up / roll_down
    rsi = 100.0 - (100.0 / (1.0 + rs))

    # Avoid division-by-zero if `roll_down` is zero
    # This prevents inf and/or nan values.
    rsi[:] = np.select([roll_down == 0, roll_up == 0, True], [100, 0, rsi])
    rsi.name = 'rsi'

    # Assert range
    valid_rsi = rsi[length - 1:]
    assert ((0 <= valid_rsi) & (valid_rsi <= 100)).all()
    # Note: rsi[:length - 1] is excluded from above assertion because it is NaN for SMA.

    return rsi

if __name__ == "__main__":
    msft = yf.Ticker(argv[1].upper())
    # get historical market data
    hist = msft.history(period="1mo")
    close = hist["Close"]
    
    rsi_ema = calculateRSI(close)
    rsi_ema = rsi_ema[-14:]
    print(rsi_ema)
    # Compare graphically
    plt.figure(figsize=(8, 6))
    rsi_ema.plot()
    plt.legend('RSI via EMA/EWMA')
    plt.show()
