class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        
        if not intervals:
            return [newInterval]
        
        if not newInterval:
            return intervals
        
        first_index = -1
        second_index = -1
        
        new_min, new_max = newInterval
        limit = len(intervals)
        
        for i, interval in enumerate(intervals):
            rng_min, rng_max = interval[0], interval[1]
            rng = range(rng_min, rng_max + 1)
            
            if first_index == -1:
                if new_min in rng:
                    first_index = i
                elif i < limit - 1:
                    if new_min > rng_max and new_min < intervals[i+1][0]:
                        first_index = i + 0.5
            
            if second_index == -1:
                if new_max in rng:
                    second_index = i
                elif i < limit - 1:
                    if new_max > rng_max and new_max < intervals[i+1][0]:
                        second_index = i + 0.5
        
        del limit, rng_min, rng_max, rng, i
        
        if (first_index, second_index) == (-1, -1):
            if new_min < intervals[0][0] and new_max > intervals[-1][1]:
                return [newInterval]
            else:
                return intervals + [newInterval] if new_min > intervals[-1][1] else [newInterval] + intervals
        elif second_index == -1:
            if first_index % 1 == 0.5:
                return intervals[:int(first_index+0.5)] + [newInterval]
            else:
                return intervals[:first_index] + [[intervals[first_index][0], new_max]]
        elif first_index == -1:
            if second_index % 2 == 0.5:
                return [newInterval] + intervals[int(second_index+0.5):]
            else:
                return [[new_min, intervals[second_index][1]]] + intervals[second_index+1:]
        else:
            first_found, second_found = not first_index % 1 == 0.5, not second_index % 1 == 0.5
            
            if first_found and second_found:
                return intervals[:first_index] + [[intervals[first_index][0], intervals[second_index][1]]] + intervals[second_index+1:]
            elif first_found and not second_found:
                return intervals[:first_index] + [[intervals[first_index][0], new_max]] + intervals[int(second_index+0.5):]
            elif not first_found and second_found:
                
                return intervals[:int(first_index+0.5)] + [[new_min, intervals[second_index][1]]] + intervals[second_index+1:]
            elif not first_found and not second_found:
                return intervals[:int(first_index+0.5)] + [[new_min, new_max]] + intervals[int(second_index+0.5):]
            
if __name__ == "__main__":
    s = Solution()
    
    intervals = [[1,5]]
    newInterval = [0,6]
    print(s.insert(intervals, newInterval))