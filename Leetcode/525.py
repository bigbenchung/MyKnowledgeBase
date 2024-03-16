class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        def getIncrement(num: int) -> int:
            return 1 if num == 1 else -1
        
        hashmap = {0: -1}
        curr_sum = 0
        curr_max = 0
        
        for i, num in enumerate(nums):
            curr_sum += getIncrement(num)
            
            if curr_sum in hashmap.keys():
                curr_max = max(curr_max, i-hashmap[curr_sum])
            else:
                hashmap[curr_sum] = i
        
        return curr_max
        
if __name__ == "__main__":
    s = Solution()
    
    nums = [0,1]
    print(s.findMaxLength(nums))