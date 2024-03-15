import yfinance as yf

import pandas as pd
import numpy as np

def getGrowth(historical_price: float, current_price: float) -> float:
    try:
        return round((current_price - historical_price) / historical_price, 2)
    except:
        return 0.00
    
def get():
    info = pd.read_csv("us_symbols.csv")
    
    all_symbols = list(info["ticker"].values)
    cleaned_symbols = list()
    for symbol in all_symbols:
        try:
            cleaned_symbols.append(symbol.strip())
        except:
            continue

    start_data = yf.download(cleaned_symbols,start='2019-2-25',end='2019-2-26')['Adj Close']
    end_data = yf.download(cleaned_symbols,start='2024-2-23',end='2024-2-24')['Adj Close']
    
    output = pd.concat([start_data, end_data])
    output.fillna(0)
    output.to_csv("all_stocks_5_year_growth.csv")
    import json
    final = json.loads(output.to_json())
    
    output_str = "ticker,growth\n"
    threshold = 10
    
    for stock, prices in final.items():
        growth = getGrowth(prices["1551052800000"], prices["1708646400000"])
        if growth > threshold:
            output_str += f"{stock},{growth}\n"
    
    with open("Top_Growers.csv", "w") as f:
        f.write(output_str)
    

if __name__ == "__main__":
    get()