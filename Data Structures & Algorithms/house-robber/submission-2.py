class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in dp:
                return dp[i]

            # Choice 1: rob this house
            rob_this = nums[i] + dfs(i + 2)
            # Choice 2: skip this house
            skip_this = dfs(i + 1)
            
            ans = max(rob_this, skip_this)
            dp[i] = ans
            return ans
        
        return dfs(0)

            

            
                

            