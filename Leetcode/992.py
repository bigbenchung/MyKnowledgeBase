from Timer import Timer

class Solution:
    
    totalTimer = Timer()
        
    def subarraysWithKDistinct(self, nums: list[int], k: int) -> int:
        def addToTracker(num, new_num_flag: bool) -> int:
            if new_num_flag:
                self.curr_tracker[num] = 1
                return 1
            else:
                self.curr_tracker[num] += 1
                return 0
            
        def removeFromTracker(num, remove_flag: bool) -> int:
            if remove_flag:
                del self.curr_tracker[num]
                return 1
            else:
                self.curr_tracker[num] -= 1
                return 0

        left = 0
        right = -1
        limit = len(nums)
        curr_len = 0
        self.curr_tracker = dict()
        counter = 0

        if limit < k:
            return 0
        elif limit == k:
            return 1
        
        for left in range(0, limit):
            if left > 0:
                curr_len -= removeFromTracker(nums[left-1], self.curr_tracker[nums[left-1]] == 1)
                if curr_len == k:
                    counter += 1
                    
                    if not decreasing:
                        while right >= left + k:
                            remove_flag = self.curr_tracker[nums[right]] == 1
                            if curr_len == k and remove_flag:
                                break
                            curr_len -= removeFromTracker(nums[right], remove_flag)
                            right -= 1
                            if curr_len == k:
                                counter += 1
                        decreasing = True
                        continue
            while right + 1 < limit:
                decreasing = False
                new_num_flag = nums[right + 1] not in self.curr_tracker.keys()
                if curr_len == k and new_num_flag:
                    break
                right += 1
                curr_len += addToTracker(nums[right], new_num_flag)
                if curr_len == k:
                    counter += 1
        return counter
    
if __name__ == "__main__":
    s = Solution()
    
    nums = [1,2,1,3,4]
    k = 3
    
    print(s.subarraysWithKDistinct(nums, k)) 
    print(s.totalTimer.getTotalTime())