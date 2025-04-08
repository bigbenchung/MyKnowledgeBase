from CodeTimer import Timer
import math

class Solution:
    
    """
    You are given an integer array nums. You need to ensure that the elements in the array are distinct. To achieve this, you can perform the following operation any number of times:

    Remove 3 elements from the beginning of the array. If the array has fewer than 3 elements, remove all remaining elements.
    Note that an empty array is considered to have distinct elements. Return the minimum number of operations needed to make the elements in the array distinct.
    """    
    totalTimer = Timer()

    def minimumOperations(self, nums: list[int]) -> int:
        distinct = set()
        operations = math.ceil(len(nums)/3)
        curr_pos, new_pos = len(nums)-1, 3*operations-4
        while operations > 0:
            for i in range(curr_pos, new_pos, -1):
                if nums[i] in distinct:
                    return operations
                distinct.add(nums[i])
            curr_pos = new_pos
            new_pos -= 3
            operations -= 1
        
        return operations

if __name__ == "__main__":
    sol = Solution()

    # 2
    nums = [1,2,3,4,2,3,3,5,7]

    print(sol.minimumOperations(nums))
    print(sol.totalTimer.getTotalTime())