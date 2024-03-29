from sys import argv

from GoldenCrossTrading import GoldenCrossTrading
from StockHelper import StockHelper

def test(principal: float, export: bool, period: str):
    tickers = list()
    with open("largestTickers.csv", "r") as f:
        lines = f.readlines()
        for line in lines:
            tickers.append(line.strip())
        
    for ticker in tickers:
        trading = GoldenCrossTrading(
            stock=StockHelper(stock_code=ticker, period=period), 
            principal=principal,
            target_n=20,
            remaining_n=[3,5,7]
        )
        trading.trade(export=export)
        trading.printDetails()
    
if __name__ == "__main__":
    principal=float(argv[1])
    export=argv[2]
    period=argv[3]
    
    test(principal, export, period)