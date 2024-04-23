from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()
    
    def minRemoveToMakeValid(self, s: str) -> str:
        
        i = len(s) - 1
        removal_tracker = set()
        close_tracker = set()

        while i >= 0:
            char = s[i]

            if char == ")":
                close_tracker.add(i)
            elif char == "(":
                if close_tracker:
                    close_tracker.pop()
                else:
                    removal_tracker.add(i)
            i -= 1
        
        removal_tracker = sorted(set.union(removal_tracker,close_tracker), reverse=True)
        
        for idx in removal_tracker:
            s = s[:idx] + s[idx+1:]

        return s
        
        

if __name__ == "__main__":
    s = Solution()
    
    string = "))(("
    
    print(s.minRemoveToMakeValid(string)) 
    print(s.totalTimer.getTotalTime())
    