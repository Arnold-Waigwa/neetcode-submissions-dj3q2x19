class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if abs(target) > total:
            return 0
        
        n = 2 * total
        dp = [[0] * (n + 1) for _ in range(len(nums) + 1)]
        
        dp[0][total] = 1  # sum = 0
        
        for i in range(1, len(nums) + 1):
            num = nums[i - 1]
            for j in range(n + 1):
                add = dp[i-1][j + num] if j + num <= n else 0
                sub = dp[i-1][j - num] if 0 <= j - num <= n else 0
                dp[i][j] = add + sub
        
        return dp[len(nums)][total + target]