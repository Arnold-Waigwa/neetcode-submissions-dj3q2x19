class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[n][m] = True

        for i in range(n, -1, -1):
            for j in range(m - 1, -1, -1):
                match = i < n and (p[j] == s[i] or p[j] == ".")
                if (j + 1) < m and p[j + 1] == "*":
                    dp[i][j] = dp[i][j + 2] or (match and dp[i + 1][j])
                else:
                    dp[i][j] = match and dp[i + 1][j + 1]
        return dp[0][0]

