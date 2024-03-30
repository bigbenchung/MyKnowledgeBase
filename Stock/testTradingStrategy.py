from sys import argv
import pandas as pd
import numpy as np

from GoldenCrossTrading import GoldenCrossTrading
from StockHelper import StockHelper

def test(principal: float, export: bool, period: str):
    all_large_tickers = pd.read_csv("./data/largestTickers.csv")
    portfolioPnL, percentageIncrease = np.array([0]*len(all_large_tickers)), np.array([0]*len(all_large_tickers))
    dfs = list()
    for i, row in all_large_tickers.iterrows():
        ticker = row["Symbol"]
        trading = GoldenCrossTrading(
            stock=StockHelper(stock_code=ticker, period=period), 
            principal=principal,
            target_n=20,
            remaining_n=[3,5,7]
        )
        dfs.append(trading.trade(export=export))
        trading.printDetails()
        portfolioPnL[i] = trading.getPnL()
        try:
            percentageIncrease[i] = trading.getEffectiveIncrease()
        except ValueError:
            print("Cannot compute stock return due to unknown error")
            continue
        
    print("-------------- Final Result --------------")
    print(f"{'Average PnL ='.ljust(45, ' ')}{np.mean(portfolioPnL)*100}%")
    print(f"{'Average Eff. increase ='.ljust(45, ' ')}{np.mean(percentageIncrease)*100}%")
    print(f"{'Percent of stocks with +ve eff. increase ='.ljust(45, ' ')}{(np.sum(percentageIncrease > 0) / percentageIncrease.size) * 100}%")
    output_df = pd.concat(dfs, axis=0)
    output_df.to_csv(f"./results/test_result_{period}.csv", index=False, header=True)
    
if __name__ == "__main__":
    principal=float(argv[1])
    export=argv[2]
    period=argv[3]
    
    test(principal, export, period)