from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()
    
    def findRotateSteps(self, ring: str, key: str) -> int:
        def getDistance(idx1: int, idx2: int) -> int:
            (idx1, idx2) = (idx2, idx1) if idx1 > idx2 else (idx1, idx2)
            return min(idx2 - idx1, idx1 + self.max_pos + 1 - idx2)

        def dfs(curr_pos: int, target_str: str) -> int:
            if not target_str:
                return 0
            
            options = set()
            for pos in self.ring_pos_tracker[target_str[0]]:
                if (pos, target_str) not in self.tracker.keys():
                    self.tracker[(pos, target_str)] = dfs(pos, target_str[1:])
                options.add(getDistance(pos, curr_pos) + 1 + self.tracker[(pos, target_str)])
            
            return min(options)
        
        self.max_pos = len(ring) - 1
        
        if self.max_pos == 0:
            return len(key)
        
        self.ring_pos_tracker = dict()
        
        for i, cell in enumerate(ring):
            try:
                self.ring_pos_tracker[cell].add(i)
            except KeyError:
                self.ring_pos_tracker[cell] = {i}
        
        self.tracker = dict()
        return dfs(0, key)
    
if __name__ == "__main__":
    sol = Solution()

    ring = "godding"
    key = "gd"
    # key = "godding"
    print(sol.findRotateSteps(ring, key))
    print(sol.totalTimer.getTotalTime())