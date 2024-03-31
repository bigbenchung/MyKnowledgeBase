from Timer import Timer

class Solution:
    
    totalTimer = Timer()

    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        
        partitions = list()
        minK_check = False
        maxK_check = False
        good_first_index = -1
        good_rng = range(minK, maxK+1)
        for i, num in enumerate(nums):
            if good_first_index == -1:
                if num in good_rng:
                    good_first_index = i
                    minK_check = num == minK
                    maxK_check = num == maxK
            else:
                minK_check = max(minK_check, num == minK)
                maxK_check = max(maxK_check, num == maxK)

                if num not in good_rng:
                    if minK_check and maxK_check:
                        partitions.append((good_first_index, i))
                    minK_check = False
                    maxK_check = False
                    good_first_index = -1
                elif i == len(nums) - 1:
                    if minK_check and maxK_check:
                        partitions.append((good_first_index, len(nums)))

        del minK_check, maxK_check, good_first_index, good_rng

        counter = 0

        for start, end in partitions:
            partition = nums[start:end]
            print(partition)
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
                                if partition[right] == minK and min_max_counter["min"] == 1:
                                    break
                                else:
                                    min_max_counter["min"] -= 1    
                                if partition[right] == maxK and min_max_counter["max"] == 1:
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
    
    nums = [35054,398719,945315,945315,820417,945315,35054,945315,171832,945315,35054,109750,790964,441974,552913]
    minK = 35054
    maxK = 945315
    
    print(s.countSubarrays(nums, minK, maxK)) 
    print(s.totalTimer.getTotalTime())