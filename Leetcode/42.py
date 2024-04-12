import numpy as np

from Timer import Timer

class Solution:
    
    totalTimer = Timer()
        
    def trap(self, height: list[int]) -> int:

        self.max_trackers = np.tile(np.array([0, 0]), (len(height), 1))
        temp_left_max = 0
        temp_right_max = 0
        
        length = len(height)
        even_len = length % 2 == 0
        half = length // 2
        
        vol = 0
        
        for i in range(0, length):
            temp_left_max = max(temp_left_max, height[i])
            temp_right_max = max(temp_right_max, height[-(i+1)])
            
            self.max_trackers[i][0] = temp_left_max if temp_left_max > height[i] else 0
            self.max_trackers[-(i+1)][1] = temp_right_max if temp_right_max > height[-(i+1)] else 0

            if i >= half:
                if i == half and not even_len:
                    vol += max(min(self.max_trackers[i][0], self.max_trackers[i][1]) - height[i], 0)
                else:
                    vol += max(min(self.max_trackers[i][0], self.max_trackers[i][1]) - height[i], 0) + \
                        max(min(self.max_trackers[-(i+1)][0], self.max_trackers[-(i+1)][1]) - height[-(i+1)], 0)
                    
        return vol
        
if __name__ == "__main__":
    s = Solution()
    
    height = [4,2,0,3,2,5]

    print(s.trap(height)) 
    print(s.totalTimer.getTotalTime())