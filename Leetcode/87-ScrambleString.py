from CodeTimer import Timer
import numpy as np

class Solution:
    
    """
    We can scramble a string s to get a string t using the following algorithm:

    If the length of the string is 1, stop.
    If the length of the string is > 1, do the following:
    Split the string into two non-empty substrings at a random index, i.e., if the string is s, divide it to x and y where s = x + y.
    Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become s = x + y or s = y + x.
    Apply step 1 recursively on each of the two substrings x and y.
    Given two strings s1 and s2 of the same length, return true if s2 is a scrambled string of s1, otherwise, return false.
    """    
    totalTimer = Timer()

    def isScramble(self, s1: str, s2: str) -> bool:
        
        def check(word1: str, word2: str) -> bool:
            if (word1, word2) in self.tracker.keys():
                return self.tracker[(word1, word2)]
            
            if len(word1) == 1:
                return word1 == word2
            
            if word1 == word2:
                return True
            
            start_set1, start_set2, end_set2 = set(), set(), set()

            for i in range(len(word1[:-1])):
                start_set1.add(word1[i])
                start_set2.add(word2[i])
                end_set2.add(word2[-i-1])

                if start_set1 == start_set2:
                    word1_s1, word1_s2 = word1[:i+1], word1[i+1:]
                    word2_s1, word2_s2 = word2[:i+1], word2[i+1:]
                    if check(word1_s1, word2_s1) and check(word1_s2, word2_s2):
                        self.tracker[(word1, word2)] = True
                        return True

                if start_set1 == end_set2:
                    word1_s1, word1_s2 = word1[:i+1], word1[i+1:]
                    word2_s1, word2_s2 = word2[-i-1:], word2[:-i-1]
                    if check(word1_s1, word2_s1) and check(word1_s2, word2_s2):
                        self.tracker[(word1, word2)] = True
                        return True
            self.tracker[(word1, word2)] = False
            return False
        
        self.tracker = dict()
        
        return check(s1, s2)


if __name__ == "__main__":
    sol = Solution()

    # True
    s1 = "abcdbdacbdac"
    s2 = "bdacabcdbdac"

    print(sol.isScramble(s1, s2))
    print(sol.totalTimer.getTotalTime())