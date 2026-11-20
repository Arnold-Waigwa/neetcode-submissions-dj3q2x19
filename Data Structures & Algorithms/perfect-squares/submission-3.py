class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = i
            for j in range(1, i):
                if j * j > i:
                    break
                dp[i] = min(dp[i], 1 + dp[i - (j * j)])
        
        return dp[-1]