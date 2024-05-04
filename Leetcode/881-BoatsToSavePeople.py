from CodeTimer import Timer

class Solution:
    
    """
    You are given an array people where people[i] is the weight of the ith person, 
    and an infinite number of boats where each boat can carry a maximum weight of limit. 
    Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

    Return the minimum number of boats to carry every given person.
    """    
    totalTimer = Timer()

    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people = sorted(people, reverse=True)
        boat_count = 0
        people_len = len(people)
        
        while people_len > 0:
            if people_len == 1:
                return boat_count + 1
            if people[-1] <= limit - people.pop(0):
                people.pop()
                people_len -= 2
            else:
                people_len -= 1
            boat_count += 1
        return boat_count
    
if __name__ == "__main__":
    sol = Solution()

    # 3
    people = [3,2,2,1]
    limit = 3

    # 4
    people = [3,5,3,4]
    limit = 5
    
    # 3
    people = [1,5,3,5]
    limit = 7
    
    # 11
    people = [2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10]
    limit = 50
    
    print(sol.numRescueBoats(people, limit))
    print(sol.totalTimer.getTotalTime())