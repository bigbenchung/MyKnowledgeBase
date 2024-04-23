from CodeTimer import Timer

class Solution:

    totalTimer = Timer()

    def checkValidString(self, s: str) -> bool:
        
        forward_counter = 0
        backward_counter = 0

        for i in range(0, len(s)):
            forward_counter += 1 if s[i] in ("(", "*") else -1
            backward_counter += 1 if s[len(s)-i-1] in (")", "*") else -1
            if forward_counter < 0 or backward_counter < 0:
                return False
        
        return forward_counter >= 0 and backward_counter >= 0

if __name__ == "__main__":
    s = Solution()
    
    string = "(*)"
    
    print(s.checkValidString(string)) 
    print(s.totalTimer.getTotalTime())