class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        
        self.output = [1 for i in range(0, len(nums))]
        prefix = 1
        suffix = 1
        
        for i in range(0, len(nums) - 1):
            right_index = len(nums)-i-1
            prefix *= nums[i]
            suffix *= nums[right_index]
            self.output[i+1] *= prefix
            self.output[right_index-1] *= suffix
        
        return self.output
                    
                    

if __name__ == "__main__":
    s = Solution()
    
    nums = [-1,1,0,-3,3]
    print(s.productExceptSelf(nums))