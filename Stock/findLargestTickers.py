import pandas as pd
from datetime import datetime

def findLargestTickers(market_cap=2000000000, avg_volume=500000, data_year=5):
    
    df = pd.read_csv("./us_symbols.csv")
    df = df[(df["Market Cap"] >= market_cap) & 
            (df["Volume"] >= avg_volume) &
            (df["IPO Year"] < datetime.now().year - data_year)]
    
    df.to_csv("largestTickers.csv", header=True, index=False)

if __name__ == "__main__":
    findLargestTickers()