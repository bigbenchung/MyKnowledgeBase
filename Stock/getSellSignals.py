from datetime import datetime

from StockHelper import StockHelper
from GoldenCrossTrading import GoldenCrossTrading
from Intersection import Intersection

def getSellSignals():
    my_tickers = list()
    
    with open("./data/portfolio.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            my_tickers.append(line.strip().upper())
    
    sell_stocks: list[tuple[StockHelper, list[Intersection]]] = list()

    for ticker in my_tickers:
        print(f"Checking {ticker}...")
        stock = StockHelper(stock_code=ticker, period="3mo")

        intersections = stock.getLineIntersections(20, [3,5,7])
        trade = GoldenCrossTrading(stock, 10000, 20, [3,5,7])
        signals: list[dict] = trade.getBuySellSignals(intersections)
        if signals:
            last_signal = signals[-1]
            if (datetime.now().date() - last_signal["date"]).days < 3:
                if last_signal["buy/sell"] == "sell":
                    sell_stocks.append((stock, intersections))

    if sell_stocks:
        for stock, intersections in sell_stocks:
            stock.plotDaysAverage([3,5,7,20], intersections)
    else:
        print("No sell signals detected.")
            
if __name__ == "__main__":
    getSellSignals()