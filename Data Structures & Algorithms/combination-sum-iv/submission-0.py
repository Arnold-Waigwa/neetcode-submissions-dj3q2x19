from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        combinations problem
        dfs(target) -> with the entire search space
        """
        @cache
        def dfs(goal):
            if goal == 0:
                return 1
            if goal < 0:
                return 0
            
            count = 0
            for num in nums:
                count += dfs(goal - num)
            
            return count
        
        return dfs(target)
        
        
