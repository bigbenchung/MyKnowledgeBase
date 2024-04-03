class KLine:
    
    """
    Types are as follows:
    0: long red -- strong, expecting further increase
    1: long black -- weak, expecting further drop
    2: short red -- unclear, may turn into long red if occur consecutively
    3: short black -- unclear, may turn into long black if occur consecutively
    4: bottom shadow red -- may indicate reaching bottom if trend is down
    5: bottom shadow black -- may indicate reaching bottom if trend is down
    6: upper shadow red -- may indicate reaching top if trend is up
    7: upper shadow black -- may indicate reaching top if trend is up
    8: cross -- usually occur during transition period
    9: grave tower -- may mean being short selled, may drop later
    """
    
    def __init__(self, open, high, low, close) -> None:
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.total_length = self.high - self.low
    
    def getRelativeLength(self, p1: float, p2: float) -> float:
        return abs(p1-p2) / self.total_length
    
    def approxEqual(self, p1: float, p2: float) -> bool:
        return True if self.getRelativeLength(p1, p2) < 0.05 else False
    
    def determineCategory(self):
        pass