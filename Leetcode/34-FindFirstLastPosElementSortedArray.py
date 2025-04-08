from CodeTimer import Timer
import math

class Solution:
    
    """
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

    If target is not found in the array, return [-1, -1].

    You must write an algorithm with O(log n) runtime complexity.
    """

    totalTimer = Timer()

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def search(num_list: list[int], starting_idx=0):
            num_list_len = len(num_list)

            if num_list_len == 0:
                return [-1, -1]
            if num_list_len == 1:
                return [-1, -1] if num_list[0] != target else [starting_idx, starting_idx]
            
            mid_idx = num_list_len // 2
            mid = num_list[mid_idx]

            if mid > target:
                return search(num_list[:mid_idx],starting_idx)
            
            if mid < target:
                return search(num_list[mid_idx+1:],starting_idx+mid_idx+1)
            
            # case when mid == target
            start, end = -1, -1
            i = 1
            while start == -1 or end == -1:
                if start == -1 and (mid_idx - i < 0 or num_list[mid_idx-i] != target):
                    start = starting_idx + mid_idx - i + 1
                if end == -1 and (mid_idx + i >= num_list_len or num_list[mid_idx+i] != target):
                    end = starting_idx + mid_idx + i - 1
                i += 1
            return [start, end]
            
        return search(nums)

if __name__ == "__main__":
    sol = Solution()

    # [3,4]
    nums = [5,7,7,8,8,10,11,11,11,11,11,11,11,11,11]
    target = 5

    print(sol.searchRange(nums, target))
    print(sol.totalTimer.getTotalTime())