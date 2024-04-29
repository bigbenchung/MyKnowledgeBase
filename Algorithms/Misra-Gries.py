class MS:
    """
    Used for Data Streaming to find up to k items that occur more than 1/k fraction of the time in a stream
    Estimate their frequencies with additive error ≤ N/(k+1)
    """
    
    def __init__(self, k: int) -> None:
        self.k = k
        self.candidates = dict()
        self.curr_len = 0
    
    def add_data(self, data: list):
        decrement = 0
        for dp in data:
            decrement += self.add_data_point(dp)
            print(self.candidates)
        # Estimated frequency interval of ele = [self.candidates[ele], self.candidates[ele]+decrement]
        print(f"decrement = {decrement}")
            
    def add_data_point(self, dp) -> int:
        """
        add a datapoint and will return int(0, 1) indicating decrement in this operation
        """
        if dp in self.candidates.keys():
            self.candidates[dp] += 1
        elif self.curr_len < self.k:
            self.candidates[dp] = 1
            self.curr_len += 1
        else:
            remove_key = set()
            for key in self.candidates.keys():
                self.candidates[key] -= 1
                if self.candidates[key] == 0:
                    remove_key.add(key)
            
            for key in remove_key:
                del self.candidates[key]
                self.curr_len -= 1
            return 1
        return 0

if __name__ == "__main__":
    data_str = "A A A C D D B B A A B B A A A B B B A A A C C C D A B A B A A"
    ms = MS(k=2)
    
    ms.add_data(data_str.split())