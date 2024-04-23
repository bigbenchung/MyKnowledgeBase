from CodeTimer import Timer

class Solution:

    totalTimer = Timer()
    
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        
        i = 0
        counter = 0
        tracker = list()
        
        while i < len(nums):
            new_num = nums[i]
            tracker.append(1)
            length = len(tracker)
            
            if not (new_num == 1 and k > 1):
                if new_num >= k:
                    tracker = list()
                    length = 0
                else:
                    limit = -(-k // new_num)
                    for j in range(length-1, -1, -1):
                        if tracker[j] >= limit:
                            tracker = tracker[j+1:]
                            length -= (j+1)
                            break
                        else:
                            tracker[j] *= new_num
            counter += length
            i += 1
            
        return counter

if __name__ == "__main__":
    s = Solution()
    nums = [10,5,2,6]
    k = 100
    print(s.numSubarrayProductLessThanK(nums, k))
    print(s.totalTimer.getTotalTime())