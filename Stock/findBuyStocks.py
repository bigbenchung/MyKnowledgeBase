import pandas as pd
from datetime import datetime

from StockHelper import StockHelper
from GoldenCrossTrading import GoldenCrossTrading
from Intersection import Intersection

def findBuyStocks():
    all_large_tickers = pd.read_csv("./data/largestTickers.csv")
    candidates_stocks: list[tuple[StockHelper, list[Intersection]]] = list()

    for i, row in all_large_tickers.iterrows():
        ticker = row["Symbol"]
        print(f"Checking {ticker}...")
        stock = StockHelper(stock_code=ticker, period="3mo")

        intersections = stock.getLineIntersections(20, [3,5,7])
        trade = GoldenCrossTrading(stock, 10000, 20, [3,5,7])
        signals: list[dict] = trade.getBuySellSignals(intersections)
        

        if signals:
            last_signal = signals[-1]
            if (datetime.now().date() - last_signal["date"]).days < 3:
                if last_signal["buy/sell"] == "buy":
                    candidates_stocks.append((stock, intersections))
        
    candidates = ""

    for stock, intersections in candidates_stocks:
        stock.plotDaysAverage([3,5,7,20], intersections)
        keep = input("Type n to discard the candidate:")
        if keep != "n":
            candidates += f"{stock.stock_code}\n"

    with open("./results/buy_candidates.txt", "w") as f:
        f.write(candidates)

def displayCandidates():
    with open("./results/buy_candidates.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            ticker = line.strip()
            stock = StockHelper(ticker,"3mo")
            stock.plotDaysAverage([3,5,7,20], stock.getLineIntersections(20, [3,5,7], 60))
            
if __name__ == "__main__":
    findBuyStocks()