import pandas as pd
from datetime import datetime as dt

class Intersection:
    """
    This class is used for denoting the properties the intersections of N days Avg Lines 
    """
    def __init__(self, n_avg: int, day: dt, up_trend: bool, targetPercentChange: float):
        self.n_avg = n_avg
        self.day = day
        self.up_trend = up_trend
        self.targetPercentChange = targetPercentChange
    