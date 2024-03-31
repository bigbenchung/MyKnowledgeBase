from Timer import Timer

class Solution:
    
    totalTimer = Timer()
    partitionTimer = Timer()
    
    def countSubarrays(self, nums: list[int], minK: int, maxK: int) -> int:
        res = 0
        bad_idx = left_idx = right_idx = -1

        for i, num in enumerate(nums) :
            if not minK <= num <= maxK:
                bad_idx = i

            if num == minK:
                left_idx = i

            if num == maxK:
                right_idx = i

            res += max(0, min(left_idx, right_idx) - bad_idx)

        return res
        

if __name__ == "__main__":
    s = Solution()
    
    nums = [1,3,5,7,9,5,1,3,5,1,3,5,4,5]
    minK = 1
    maxK = 5
    
    print(s.countSubarrays(nums, minK, maxK)) 
    print(s.totalTimer.getTotalTime())
    