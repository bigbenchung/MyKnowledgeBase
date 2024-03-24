from Timer import Timer

class Solution:

    totalTimer = Timer()

    """
    Edit Distance is calculated dynamically with the following matrix:
        r   o   s
    h   0   0   0
    o   0   1   0
    r   1   0   0
    s   0   0   1
    e   0   0   0

    Three actions are allowed -- Insert, Delete and Replace
    Insert -- add a new row
    Delete -- ignore a row
    Replace -- fill a cell with 1

    End goal:
        r   o   s
    r   1   0   0   -- Replace h with r
    o   0   1   0   
    r   1   0   0   -- Removed r (ignored)
    s   0   0   1
    e   0   0   0   -- Removed e (ignored)
    """

    def minDistance(self, word1: str, word2: str) -> int:
        
        def generateMatrix(word1: str, word2: str) -> list[list[int]]:
            matrix = list()
            for char1 in word1:
                matrix.append(list())
                for char2 in word2:
                    matrix[-1] += [1] if char1 == char2 else [0]
            return matrix
        
        def getDistance(row: int, col: int):
            def insert() -> int:
                try:
                    if col + 1 < self.max_col:
                        return 1 + getDistance(row, col+1) if row + 1 < self.max_row else self.max_col - col - 1
                    return None
                except TypeError:
                    return None
            
            def delete() -> int:
                try:
                    return 1 + getDistance(row+1, col) if row + 1 < self.max_row else None
                except TypeError:
                    return None
            
            def replace() -> int:
                try:
                    if row + 1 < self.max_row and col + 1 < self.max_col:
                        return 1 + getDistance(row+1, col+1)
                    elif col + 1 == self.max_col:                   # Reached last col
                        return self.max_row - row
                    elif row + 1 == self.max_row:                   # Reached last row
                        return self.max_col - col
                except TypeError:
                    return None
            
            if (row, col) in self.tracker.keys():
                return self.tracker[(row, col)]

            if self.str_matrix[row][col] == 1:
                options = list()
                if col + 1 < self.max_col:
                    if row + 1 < self.max_row:
                        options.append(getDistance(row+1, col+1))
                    options += [delete(), insert()]
                elif row + 1 < self.max_row:                            # Reached last col and found
                    self.tracker[(row, col)] = self.max_row - row - 1   # Remove the remaining rows
                    return self.tracker[(row, col)]
                else:
                    return 0
            else:
                if col + 1 < self.max_col and row + 1 < self.max_row:
                    options = [insert(), delete(), replace()]
                elif col + 1 == self.max_col:                           # Reached last col but 0
                    options = [replace(), delete()]
                elif row + 1 == self.max_row:                           # Reached last row and not last col but 0
                    have_one = False
                    for i in range(col+1, self.max_col):
                        if self.str_matrix[row][i] == 1:
                            have_one = True
                            break
                    options = [insert()] if have_one else [replace()]
            options = [option for option in options if option != None]
            self.tracker[(row, col)] = min(options) if options else None
            return self.tracker[(row, col)]

        
        if not word1:
            return len(word2)

        if not word2:
            return len(word1)
                        
        self.str_matrix = generateMatrix(word1, word2)
        self.max_row, self.max_col = len(self.str_matrix), len(self.str_matrix[0]) 
        self.tracker = dict()
        
        return getDistance(0, 0)

if __name__ == "__main__":
    s = Solution()
    
    word1 = "mart"
    word2 = "kar"
    print(s.minDistance(word1, word2))
    print(s.tracker)
    print(s.totalTimer.getTotalTime())