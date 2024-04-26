from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()
    
    def minFallingPathSum(self, grid: list[list[int]]) -> int:
        
        def form_prev_row_info(row: list[int]):
            def get_element(idx: int, val: int) -> tuple[int, int]:
                return (idx, val+min1) if idx != idx1 else (idx, val+min2)
            
            [(idx1, min1), (idx2, min2)] = self.prev_row_info if self.prev_row_info else [(-1, 0), (-1, 0)]
            
            temp = sorted([get_element(0, row[0]), get_element(1, row[1])], key=lambda x: x[1])
            for i, num in enumerate(row[2:]):
                new_ele = get_element(i+2, num)
                if new_ele[1] < temp[1][1]:
                    temp = [temp[0], new_ele] if new_ele[1] in range(temp[0][1], temp[1][1]) else [new_ele, temp[0]]
            return temp
        
        self.shape = len(grid)
        
        if self.shape == 1:
            return grid[0][0]
        
        self.prev_row_info = list()

        for i in range(self.shape-1, -1, -1):
            self.prev_row_info = form_prev_row_info(grid[i])

        return self.prev_row_info[0][1]

if __name__ == "__main__":
    sol = Solution()

    grid = [[1,2,3],[4,5,6],[7,8,9]]

    print(sol.minFallingPathSum(grid))
    print(sol.totalTimer.getTotalTime())