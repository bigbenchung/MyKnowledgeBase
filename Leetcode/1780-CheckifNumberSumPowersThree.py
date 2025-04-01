from CodeTimer import Timer
import numpy as np

class Solution:
    
    """
    Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

    An integer y is a power of three if there exists an integer x such that y == 3x.
    """    
    totalTimer = Timer()

    def checkPowersOfThree(self, n: int) -> bool:
        def search(k: int) -> bool:
            if k == 0:
                return True
            return False if k % 3 == 2 else True and search(k // 3)
        return search(n)


if __name__ == "__main__":
    sol = Solution()

    n = 12
    # true

    n = 21
    # false

    n = 91
    # true

    print(sol.checkPowersOfThree(n))
    print(sol.totalTimer.getTotalTime())