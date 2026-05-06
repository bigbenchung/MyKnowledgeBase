from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()

    def rotateTheBox(self, boxGrid: list[list[str]]) -> list[list[str]]:
        row, col = len(boxGrid), len(boxGrid[0])

        ans = [list() for c in range(col)]
        
        for r in range(row - 1, -1, -1):
            stone, empty = 0, 0
            last_update_row = 0
            for c in range(col):
                # do until reach an obstacle, divide sub sections by obstacles and reset when hit
                if boxGrid[r][c] == "#":
                    stone += 1
                elif boxGrid[r][c] == ".":
                    empty += 1

                # obstacle case / last case
                if boxGrid[r][c] == "*" or c == col - 1:
                    while empty > 0:
                        ans[last_update_row] += ["."]
                        last_update_row += 1
                        empty -= 1
                    while stone > 0:
                        ans[last_update_row] += ["#"]
                        last_update_row += 1
                        stone -= 1
                        
                    if boxGrid[r][c] == "*":
                        ans[last_update_row] += ["*"]
                        last_update_row += 1
        
        return ans
    
if __name__ == "__main__":
    s = Solution()

    boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
    
    print(s.rotateTheBox(boxGrid))
    print(s.totalTimer.getTotalTime())