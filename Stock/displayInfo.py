from StockHelper import StockHelper
from sys import argv

def displayInfo(option: str):
    if option == "portfolio":
        file_path = "./data/portfolio.txt"
    elif option == "market":
        file_path = "./data/key_indicators.txt"
        
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            ticker = line.strip()
            stock = StockHelper(ticker,"3mo")
            stock.plotDaysAverage([3,5,7,20], stock.getLineIntersections(20, [3,5,7], 60))

if __name__ == "__main__":
    try:
        option = argv[1]
    except:
        option = "portfolio"
    displayInfo(option=option)