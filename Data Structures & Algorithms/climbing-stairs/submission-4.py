class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def dfs(i):
            if i in dp:
                return dp[i]
            if i >= n:
                return i == n
            ans = dfs(i + 1) + dfs(i + 2)
            dp[i] = ans
            return ans

        return dfs(0)