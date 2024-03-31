from Timer import Timer

class Solution:
    
    totalTimer = Timer()

    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        if minK == maxK and len(set(nums)) == 1:
            return 0 if nums[0] != minK else sum([len(nums) - partition_size + 1 for partition_size in range(1, len(nums) + 1)])
        
        k = 1 if minK == maxK else 2
        partitions = list()
        minK_check = False
        maxK_check = False
        good_first_index = -1
        good_rng = range(minK, maxK+1)

        for i, num in enumerate(nums):
            if good_first_index == -1:
                if num in good_rng:
                    left = i
            else:
                

        del minK_check, maxK_check, good_first_index, good_rng

        counter = 0

        for start, end in partitions:
            partition = nums[start:end]
            right = -1
            min_max_counter = {"min": 0, "max": 0}
            for left in range(len(partition)):
                if left > 0:
                    min_max_counter["min"] -= 1 if partition[left-1] == minK else 0
                    min_max_counter["max"] -= 1 if partition[left-1] == maxK else 0

                    if min_max_counter["min"] > 0 and min_max_counter["max"] > 0:
                        counter += 1

                        if not decreasing:
                            while right >= left + 1:
                                if partition[right] == minK:
                                    if min_max_counter["min"] == 1:
                                        break
                                    
                                    else:
                                        min_max_counter["min"] -= 1    
                                if partition[right] == maxK:
                                    if min_max_counter["max"] == 1:
                                        break
                                    else:
                                        min_max_counter["max"] -= 1
                                right -= 1
                                counter += 1

                            decreasing = True
                            continue

                while right + 1 < len(partition):
                    decreasing = False
                    right += 1
                    new_num = partition[right]
                        
                    min_max_counter["min"] += 1 if new_num == minK else 0
                    min_max_counter["max"] += 1 if new_num == maxK else 0

                    if min_max_counter["min"] > 0 and min_max_counter["max"] > 0:
                        counter += 1
        return counter
        

if __name__ == "__main__":
    s = Solution()
    
    nums = [1,1,1,1]
    minK = 1
    maxK = 1
    
    print(s.countSubarrays(nums, minK, maxK)) 
    print(s.totalTimer.getTotalTime())