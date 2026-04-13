class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = 2 * sum(nums)
        if abs(target) > sum(nums):
            return 0
        dp = [[0] * (n + 1) for _ in range(len(nums) + 1)]
        dp[-1][sum(nums) + target] = 1

        for i in range(len(nums) - 1, -1, -1):
            for j in range(n, -1, -1):
                add = dp[i+1][j + nums[i]] if (j + nums[i]) <= n else 0
                sub = dp[i+1][j - nums[i]] if 0 <= (j - nums[i]) <= n else 0
                dp[i][j] = add + sub
        
        return dp[0][sum(nums)]