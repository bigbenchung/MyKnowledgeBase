import time

class Timer:
    
    def __init__(self):
        self.start_time = time.time()
        self.total_lap_time = 0
        
    def getTotalTime(self):
        return time.time() - self.start_time

    def startLap(self):
        self.lap_start_time = time.time()
    
    def endLap(self):
        self.total_lap_time += time.time() - self.lap_start_time
    
    def getTotalLapTime(self):
        return self.total_lap_time