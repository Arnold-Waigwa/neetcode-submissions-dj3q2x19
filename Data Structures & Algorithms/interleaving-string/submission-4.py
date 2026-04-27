class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)

        if m + n != p:
            return False
        
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for i in range(m + 1):
            for j in range(n + 1):
                k = i + j
                if k == 0:
                    continue
                left = dp[i][j - 1] and s2[j - 1] == s3[k - 1] if (j - 1) >= 0 else False
                right = dp[i - 1][j] and s1[i - 1] == s3[k - 1] if (i - 1) >= 0 else False
                dp[i][j] = left or right
        return dp[m][n]