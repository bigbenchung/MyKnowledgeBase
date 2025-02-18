from CodeTimer import Timer
import numpy as np

class Solution:
    
    """
    You are given a 0-indexed string pattern of length n consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

    A 0-indexed string num of length n + 1 is created using the following conditions:

    num consists of the digits '1' to '9', where each digit is used at most once.
    If pattern[i] == 'I', then num[i] < num[i + 1].
    If pattern[i] == 'D', then num[i] > num[i + 1].
    Return the lexicographically smallest possible string num that meets the conditions.
    """    
    totalTimer = Timer()

    def smallestNumber(self, pattern: str) -> str:
        self.numbers = {"1","2","3","4","5","6","7","8","9"}
        self.numbers_lst = ["1","2","3","4","5","6","7","8","9"]
        self.required_digits = len(pattern)+1

        def dfs(last_num: str, pt: str, required_len:int, used:set[str]) -> str:
            avail = self.numbers.difference(used)
            if not pt:
                for n in self.numbers_lst:
                    if n in avail:
                        return last_num + n
                    return last_num
                
            _type, pt = pt[0], pt[1:]
            avail_lst = [n for n in self.numbers_lst if n in avail and int(n) > int(last_num)] if _type == "I" \
                else [n for n in self.numbers_lst if n in avail and int(n) < int(last_num)]
            if avail_lst:
                if not _type:
                    return avail_lst[0]
                else:
                    for digit in avail_lst:
                        ans = last_num + dfs(digit,pt,required_len-1,used.union({digit}))
                        if len(ans) == required_len:
                            return ans
            return ""
        
        for n in self.numbers_lst:
            answer = dfs(n, pattern, self.required_digits, {n})
            if len(answer) == self.required_digits:
                return answer


if __name__ == "__main__":
    sol = Solution()

    pattern = "IIIDIDDD"
    # Output: "123549876"

    pattern = "DDD"
    # Output: "4321"
    print(sol.smallestNumber(pattern))
    print(sol.totalTimer.getTotalTime())