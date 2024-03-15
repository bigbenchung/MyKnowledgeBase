class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        def computeSubsequenceNo(count: int) -> int:
            return sum([count - partition_size + 1 for partition_size in range(1, count + 1)])
        
        def getBorderZeroesComb(num1, num2) -> int:
            return (num1+1) * (num2+1)
                
        prev_num = None
        self.tracker = list()
        first_1_index = 0
        left_border_1s_zeroes = dict()
        right_border_1s_zeroes = dict()
        
        for num in nums:
            if prev_num != None:
                if num == prev_num:
                    self.tracker[-1] += 1
                else:
                    prev_num = num
                    self.tracker.append(1)
            else:
                first_1_index = 0 if num == 1 else 1
                prev_num = num
                self.tracker.append(1)
                
        counter = 0
        
        if goal == 0:
            first_0_index = 1 if first_1_index == 0 else 0
            for i in range(first_0_index, len(self.tracker), 2):
                counter += computeSubsequenceNo(self.tracker[i])
        else:
            one_counter = 0
            # Initailize the borders
            for i in range(first_1_index, len(self.tracker), 2):
                if i > 0:
                    left_border_1s_zeroes[one_counter] = self.tracker[i-1]
                one_counter += self.tracker[i]
                if i < len(self.tracker) - 1:
                    right_border_1s_zeroes[one_counter-1] = self.tracker[i+1]
            distance = goal - 1
            for left in range(0, one_counter - distance):
                right = left + distance
                
                left_zeros = left_border_1s_zeroes[left] if left in left_border_1s_zeroes.keys() else 0
                right_zeros = right_border_1s_zeroes[right] if right in right_border_1s_zeroes.keys() else 0

                counter += getBorderZeroesComb(left_zeros, right_zeros)

        return counter
            
                    
                    

if __name__ == "__main__":
    s = Solution()
    
    nums = [0,0,0,0,0]
    goal = 0
    print(s.numSubarraysWithSum(nums, goal))