from CodeTimer import Timer

import numpy as np

class Solution:
    
    totalTimer = Timer()
        
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        tracker = np.zeros((n, n))
        max_seen_idx = 0

        for _from, _to in edges:
            (_from, _to) = (_to, _from) if _from > _to else (_from, _to)

            max_seen_idx = max(max_seen_idx, _to)

            for i in range(max_seen_idx+1):
                if i not in (_from, _to):
                    increment = 1 + np.count_nonzero(tracker[_from])
                    tracker[i][_to] += increment
                    tracker[_to][i] += increment
            tracker[_to][_from] = 1
            tracker[_from][_to] = 1
            print(tracker)
        
            
if __name__ == "__main__":
    solution = Solution()

    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    # edges = [[0,1],[1,2],[2,3],[3,4]]
    print(solution.sumOfDistancesInTree(n, edges))