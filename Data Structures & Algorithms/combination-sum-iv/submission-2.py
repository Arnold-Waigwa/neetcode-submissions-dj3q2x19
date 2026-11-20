from functools import cache
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        combinations problem
        dfs(target) -> with the entire search space
        dp[target] -> try every num and see whether 
        """
        dp = [0] * (target + 1)
        dp[0] = 1

        for i in range(1, target + 1):
            for num in nums:
                if num <= i:
                    dp[i] += dp[i - num]
        
        return dp[target]


        
        
