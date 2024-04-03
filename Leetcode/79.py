from Timer import Timer

class Solution:
    
    totalTimer = Timer()
    
    def exist(self, board: list[list[str]], word: str) -> bool:
        def search(node: list[int, int], pos: int, prev: set) -> bool:
            
            new_prev = set.union(prev, {node})
            
            if pos == self.word_len:
                return False
            
            target_char = word[pos]
            
            if target_char not in self.node_tracker[node].keys():
                return False
            
            possibilities = list()
            for new_node in self.node_tracker[node][target_char]:
                if new_node not in prev:
                    if pos == self.word_len - 1:
                        return True
                    possibilities.append(search(new_node, pos+1, new_prev))

            if possibilities:
                return max(possibilities)
            
            return False
        
        def addToNode(node: tuple[int, int], r: int, c: int):
            
            char = board[r][c]
            if char not in self.node_tracker[node]:
                self.node_tracker[node][char] = {(r,c)}
            else:
                self.node_tracker[node][char].add((r,c))
            
            
        self.m = len(board)
        self.n = len(board[0])
        self.word_len = len(word)
        self.target_chars = set(word)
        self.node_tracker = dict()
        target_nodes = set()
        
        for row in range(self.m):
            for col in range(self.n):
                node = (row, col)
                if board[row][col] == word[0]:
                    target_nodes.add(node)
                    
                self.node_tracker[node] = dict()
                
                if row > 0 and board[row-1][col] in self.target_chars:
                    addToNode(node, row-1, col)
                if col > 0 and board[row][col-1] in self.target_chars:
                    addToNode(node, row, col-1)
                if row < self.m - 1 and board[row+1][col] in self.target_chars:
                    addToNode(node, row+1, col)
                if col < self.n - 1 and board[row][col+1] in self.target_chars:
                    addToNode(node, row, col+1)
        
        if self.word_len == 1 and target_nodes:
            return True
        
        for node in target_nodes:
            if search(node, 1, set()):
                return True

        return False

if __name__ == "__main__":
    s = Solution()
    board=[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word="ABCB"
    print(s.exist(board, word))
    print(s.totalTimer.getTotalTime())