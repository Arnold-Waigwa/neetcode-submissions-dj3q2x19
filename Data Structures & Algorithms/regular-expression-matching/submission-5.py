class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        prev = [False] * (m + 1)
        prev[m] = True

        for j in range(m, -1, -1):
            if (j + 1) < m and p[j + 1] == "*":
                prev[j] = prev[j + 2]
        
        for i in range(n - 1, -1, -1):
            dp = [False] * (m + 1)
            for j in range(m - 1, -1, -1):
                match = s[i] == p[j] or p[j] == "."
                if (j + 1) < m and p[j + 1] == "*":
                    dp[j] = dp[j + 2] or (match and prev[j])
                else:
                    dp[j] = match and prev[j + 1]
            prev = dp[:]

        return prev[0]
