from Timer import Timer

class Solution:
    
    totalTimer = Timer()
        
    def countSubarrays(self, nums: list[int], k: int) -> int:

        max_ele = max(nums)
        temp_count = 0
        max_ele_border_tracker = list()
        temp_sum = 0
        counter = 0
        exceeded = False
        next_index_tracker = 0
        
        for num in nums:
            if num == max_ele:
                if not exceeded:
                    exceeded = len(max_ele_border_tracker) >= k
                if exceeded:
                    temp_sum += max_ele_border_tracker[next_index_tracker] + 1
                    counter += temp_sum * (temp_count + 1)
                    next_index_tracker += 1
                
                max_ele_border_tracker.append(temp_count)        
                temp_count = 0
            else:
                temp_count += 1
        
        if len(max_ele_border_tracker) >= k:
            counter += (temp_sum + max_ele_border_tracker[next_index_tracker] + 1) * (temp_count + 1)

        return counter
                    
if __name__ == "__main__":
    s = Solution()
    
    nums = [1,3,2,3,3]
    k = 2
    
    print(s.countSubarrays(nums, k)) 
    print(s.totalTimer.getTotalTime())