from CodeTimer import Timer

import numpy as np

class Solution:
    
    totalTimer = Timer()
        
    def sumOfDistancesInTree(self, n: int, edges: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        count = [1] * n
        res = [0] * n

        def dfs(node, parent):
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    count[node] += count[child]
                    res[node] += res[child] + count[child]

        def dfs2(node, parent):
            for child in graph[node]:
                if child != parent:
                    res[child] = res[node] - count[child] + (n - count[child])
                    dfs2(child, node)

        dfs(0, -1)
        dfs2(0, -1)
        
        return res
            
if __name__ == "__main__":
    solution = Solution()

    n = 6
    edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
    # edges = [[0,1],[1,2],[2,3],[3,4]]
    print(solution.sumOfDistancesInTree(n, edges))