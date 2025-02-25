from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()

    def isMatch(self, s: str, p: str) -> bool:
        
        if s == p:
            return True
        
        if "*" not in p and len(s) != len(p):
            return False
        
        if "*" in p and len(set(p)) == 1:
            return True
        
        if not s:
            return False
        
        # Pre-process to remove consecutive "*"s
        temp = ""
        current_char = None
        for char in p:
            if char != current_char:
                current_char = char
            else:
                if char == "*":
                    continue
            temp += char
        
        p = temp
        
        del temp, current_char, char
        
        self.matrix = list()
        seen_str = dict()
        for row, p_str in enumerate(p):
            if p_str in {"?", "*"}:
                self.matrix.append([1]*len(s))
            elif p_str not in seen_str.keys():
                self.matrix.append(list())
                for s_str in s:
                    self.matrix[-1] += [1] if p_str == s_str else [0]
                seen_str[p_str] = self.matrix[-1]
            else:
                self.matrix.append(seen_str[p_str])
        
        del seen_str

        self.node_tracker = dict()

        def checkPath(row: int, col: int):
            def toResult(result:bool):
                self.node_tracker[(row, col)] = result
                return result

            if row == len(p) - 1 and col == len(s) - 1:
                return self.matrix[row][col] == 1
            
            if (row, col) in self.node_tracker.keys():
                return self.node_tracker[(row, col)]
            
            if p[row] != "*":
                if col != len(s) - 1 and row != len(p) - 1 and self.matrix[row][col] == 1:
                    return toResult(checkPath(row+1, col+1) if self.matrix[row][col] == 1 else False)
                elif col == len(s) - 1 and self.matrix[row][col] == 1:
                    return toResult(p[row+1] == "*" and row+1 == len(p) - 1)
                else:
                    return toResult(False)
                
            # Separate case for *
            else:
                # if last row / col
                if row == len(p) - 1:
                    return toResult(True)

                options = list()
                for counter, cell in enumerate(self.matrix[row+1][col:]):
                    if cell == 1:
                        options.append(checkPath(row + 1, counter + col))
                return toResult(max(options) if options else False)
        
        return checkPath(0,0)
                
            
    
if __name__ == "__main__":
    sol = Solution()

    s = "aab"
    p = "c*a*b"

    print(sol.isMatch(s, p))
    print(sol.totalTimer.getTotalTime())