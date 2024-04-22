from Timer import Timer
from queue import PriorityQueue

class Solution:
    
    totalTimer = Timer()

    def openLock(self, deadends: list[str], target: str) -> int:
        
        def getDistance(coor: tuple[int, int, int, int]) -> float:
            if coor not in self.distance_tracker.keys():
                self.distance_tracker[coor] = pow(sum([pow(min(coor[i], 10-coor[i]), 2) for i in range(0, 4)]), 0.5)
            return self.distance_tracker[coor]
        
        def getNextNum(num: int, direction: int) -> int:
            if (num, direction) == (0, -1):
                return 9
            if (num, direction) == (9, 1):
                return 0
            return num + direction

        def getOptions(coor: tuple[int, int, int, int]) -> list[tuple[int, int, int, int]]:
            directions = (1, -1)
            options = list()
            for i, dimension in enumerate(coor):
                for direction in directions:
                    option = coor[0:i] + (getNextNum(dimension, direction),) + coor[i+1:]
                    if option not in self.visited and option not in self.deadends:
                        options.append(option)
            return options
        
        self.target = (int(target[0]), int(target[1]), int(target[2]), int(target[3]))
        self.visited = set()
        
        self.deadends = set()
        for deadend in deadends:
            self.deadends.add((int(deadend[0]), int(deadend[1]), int(deadend[2]), int(deadend[3])))

        if not getOptions(self.target) or not getOptions((0,0,0,0)) or (0, 0, 0, 0) in self.deadends:
            return -1
        
        self.distance_tracker = dict()
        
        # Queue object = (distance, (coor, path_len))
        q = PriorityQueue()
        q.put((getDistance(self.target), (self.target, 0)))
        
        while not q.empty():
            d, (coor, path_len) = q.get()
            
            self.visited.add(coor)
            
            if coor in self.deadends:
                continue
            
            if coor == (0, 0, 0, 0):
                return path_len
            
            options = getOptions(coor)
            
            if not options:
                self.deadends.add(coor)
            else:
                for new_coor in options:
                    q.put((getDistance(new_coor), (new_coor, path_len + 1)))
        
        return -1
            
    
if __name__ == "__main__":
    s = Solution()

    deadends = ["1000","0100","0010","0001","9000","0900","0090","0009"]
    target = "0202"
    
    # deadends = ["0201","0101","0102","1212","2002"]
    # target = "0202"
    print(s.openLock(deadends, target))
    print(s.totalTimer.getTotalTime())