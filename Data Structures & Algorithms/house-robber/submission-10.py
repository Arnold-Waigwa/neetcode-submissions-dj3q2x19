class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = max(
                dp[i + 1],
                dp[i + 2] + nums[i]
            )
        
        return dp[0]

        