class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        n = 2 * total

        if (total + target) > n:
            return 0

        dp = [0] * (n + 1)

        dp[total] = 1

        for num in nums:
            temp = dp[:]
            for val in range(n + 1):
                add = dp[val - num] if (val - num) >= 0 else 0
                sub = dp[val + num] if (val + num) <= n else 0
                temp[val] = add + sub
            dp = temp
        
        return dp[total + target]