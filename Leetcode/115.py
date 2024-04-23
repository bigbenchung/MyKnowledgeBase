import numpy as np

from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()
        
    def numDistinct(self, s: str, t: str) -> int:
        
        max_col, max_row = len(t), len(s)

        if max_col > max_row:
            return 0
        
        if max_col == max_row:
            return 1 if s == t else 0
        
        if max_row == 1:
            return s.count(t)
        
        self.tracker = dict()

        def proceed(row: int, col: int) -> int:
            
            if (row, col) in self.tracker.keys():
                return self.tracker[(row, col)]
            
            identical = s[row] == t[col]

            if col == max_col - 1:
                if row == max_row - 1:
                    return 1 if identical else 0
                else:
                    self.tracker[(row, col)] = 1 + proceed(row + 1, col) if identical else proceed(row + 1, col)
                    return self.tracker[(row, col)]
            
            if row == max_row - 1:
                self.tracker[row, col] = 0
                return 0

            options = [(row + 1, col)]

            if identical:
                options.append((row + 1, col + 1))
            
            self.tracker[(row, col)] = sum([proceed(r, c) for r, c in options])
            return self.tracker[(row, col)]
        
        return proceed(0, 0)
        
if __name__ == "__main__":
    solution = Solution()

    s = "babgbag"
    t = "bag"

    print(solution.numDistinct(s, t))
    print(solution.tracker)
    print(solution.totalTimer.getTotalTime())