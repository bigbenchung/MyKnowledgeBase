from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()
        
    def countSubarrays(self, nums: list[int], k: int) -> int:

        max_ele = max(nums)
        max_ele_border_tracker = list()
        max_ele_counter = 0
        
        temp_count = 0
        temp_sum = 0
        counter = 0
        next_index_tracker = -1
        
        for num in nums:
            if num == max_ele:
                if next_index_tracker < 0:
                    if max_ele_counter == k:
                        next_index_tracker = 0
                    else:
                        max_ele_counter += 1
                        
                if next_index_tracker >= 0:
                    temp_sum += max_ele_border_tracker[next_index_tracker] + 1
                    counter += temp_sum * (temp_count + 1)
                    next_index_tracker += 1
                
                max_ele_border_tracker.append(temp_count)
                temp_count = 0
            else:
                temp_count += 1
        
        if max_ele_counter == k:
            counter += (temp_sum + max_ele_border_tracker[max(next_index_tracker, 0)] + 1) * (temp_count + 1)

        return counter
                    
if __name__ == "__main__":
    s = Solution()
    
    nums = [165,135,165,46,126,165,73,165,165,155,150,165,40,38,165,145,137,106,10]
    k = 7
    
    print(s.countSubarrays(nums, k)) 
    print(s.totalTimer.getTotalTime())