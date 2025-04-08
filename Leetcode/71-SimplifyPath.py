from CodeTimer import Timer
import math

class Solution:
    
    """
    You are given an absolute path for a Unix-style file system, which always begins with a slash '/'. Your task is to transform this absolute path into its simplified canonical path.

    The rules of a Unix-style file system are as follows:

    A single period '.' represents the current directory.
    A double period '..' represents the previous/parent directory.
    Multiple consecutive slashes such as '//' and '///' are treated as a single slash '/'.
    Any sequence of periods that does not match the rules above should be treated as a valid directory or file name. For example, '...' and '....' are valid directory or file names.
    The simplified canonical path should follow these rules:

    The path must start with a single slash '/'.
    Directories within the path must be separated by exactly one slash '/'.
    The path must not end with a slash '/', unless it is the root directory.
    The path must not have any single or double periods ('.' and '..') used to denote current or parent directories.
    Return the simplified canonical path.
    """

    totalTimer = Timer()

    def simplifyPath(self, path: str) -> str:
        elements = path.split("/")
        output_path = list()

        for element in elements:
            if element:
                if element == "..":
                    if output_path:
                        output_path = output_path[:-1]
                elif element != ".":
                    output_path.append(element)

        return "/"+"/".join(output_path)
    
if __name__ == "__main__":
    sol = Solution()

    # /home/foo
    path = "/home//foo/"

    # "/.../b/d"
    path = "/.../a/../b/c/../d/./"
    print(sol.simplifyPath(path))
    print(sol.totalTimer.getTotalTime())