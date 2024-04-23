import numpy as np

from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()
        
    def trap(self, height: list[int]) -> int:
        
        length = len(height)
        
        max_trackers = np.tile(np.array([0, 0]), (len(height), 1))
        
        temp_left_max = 0
        temp_right_max = 0
        
        for i in range(0, length):
            temp_left_max = max(temp_left_max, height[i])
            temp_right_max = max(temp_right_max, height[-(i+1)])
            
            max_trackers[i][0] = temp_left_max
            max_trackers[-(i+1)][1] = temp_right_max
        
        del temp_left_max, temp_right_max

        vol = 0
        
        for i in range(0, length):
            vol += max(min(max_trackers[i][0], max_trackers[i][1]) - height[i], 0)
                    
        return vol
        
if __name__ == "__main__":
    s = Solution()
    
    height = [4,2,0,3,2,5]

    print(s.trap(height)) 
    print(s.totalTimer.getTotalTime())