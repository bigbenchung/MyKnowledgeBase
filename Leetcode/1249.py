from Timer import Timer

class Solution:
    
    totalTimer = Timer()
    
    def minRemoveToMakeValid(self, s: str) -> str:
        
        i = len(s) - 1
        removal_tracker = list()
        close_tracker = list()

        while i >= 0:
            char = s[i]

            if char == ")":
                close_tracker.append(i)
            elif char == "(":
                if close_tracker:
                    close_tracker.pop()
                else:
                    removal_tracker.append(i)
            i -= 1
        
        removal_tracker = sorted(removal_tracker + close_tracker, reverse=True)

        for idx in removal_tracker:
            s = s[:idx] + s[idx+1:]

        return s
        
        

if __name__ == "__main__":
    s = Solution()
    
    string = "))(("
    
    print(s.minRemoveToMakeValid(string)) 
    print(s.totalTimer.getTotalTime())
    