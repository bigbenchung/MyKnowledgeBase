from CodeTimer import Timer
import numpy as np

class Solution:
    
    """
    You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].

    The array describes the questions of an exam, where you have to process the questions in order (i.e., starting from question 0) and make a decision whether to solve or skip each question. Solving question i will earn you pointsi points but you will be unable to solve each of the next brainpoweri questions. If you skip question i, you get to make the decision on the next question.

    For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
    If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
    If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to solve questions 2 and 3.
    Return the maximum points you can earn for the exam.
    """    
    totalTimer = Timer()

    def mostPoints(self, questions: list[list[int]]) -> int:
        # key=idx, val=max_preceeding_points
        self.tracker = dict()
        self.boundary = len(questions) - 1
        
        def dfs(idx: int) -> int:
            if idx > self.boundary:
                return 0
            
            if idx not in self.tracker.keys():
                # can choose to take / skip if not last element
                pt, skip_len = questions[idx]
                
                options = [pt + dfs(idx+skip_len+1)]
                
                if idx < self.boundary:
                    options += [dfs(idx+1)]
                
                self.tracker[idx] = max(options)
                
            return self.tracker[idx]
        
        return dfs(0)
    
if __name__ == "__main__":
    sol = Solution()
    
    # 5
    questions = [[3,2],[4,3],[4,4],[2,5]]
    
    # 7
    questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    
    print(sol.mostPoints(questions))
    print(sol.totalTimer.getTotalTime())