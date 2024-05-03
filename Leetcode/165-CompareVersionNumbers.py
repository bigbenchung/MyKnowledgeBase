from CodeTimer import Timer

class Solution:
    
    totalTimer = Timer()
    
    def compareVersion(self, version1: str, version2: str) -> int:
        def check(pos: int, version_no: int) -> int:
            version_lst = self.v1_lst if version_no == 1 else self.v2_lst
            
            for str_num in version_lst[pos:]:
                if int(str_num) > 0:
                    return 1 if version_no == 1 else -1
            return 0
        
        self.v1_lst, self.v2_lst = version1.split("."), version2.split(".")
        
        for i in range(max(len(self.v1_lst), len(self.v2_lst))):
            try:
                v1_no = int(self.v1_lst[i])
            except IndexError:
                return check(i, 2)
            try:
                v2_no = int(self.v2_lst[i])
            except IndexError:
                return check(i, 1)

            if v1_no > v2_no:
                return 1
            elif v2_no > v1_no:
                return -1
        
        return 0
    
if __name__ == "__main__":
    sol = Solution()

    version1 = "1.1"
    version2 = "1.1.1"
    
    print(sol.compareVersion(version1, version2))
    print(sol.totalTimer.getTotalTime())