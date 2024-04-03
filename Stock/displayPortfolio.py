from StockHelper import StockHelper

def displayPortfolio():
    with open("./data/portfolio.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            ticker = line.strip()
            stock = StockHelper(ticker,"3mo")
            stock.plotDaysAverage([3,5,7,20], stock.getLineIntersections(20, [3,5,7], 60))

if __name__ == "__main__":
    displayPortfolio()