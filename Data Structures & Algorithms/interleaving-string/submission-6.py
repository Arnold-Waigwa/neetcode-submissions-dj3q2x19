class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n, p = len(s1), len(s2), len(s3)

        if m + n != p:
            return False

        dp = [False] * (n + 1)
        dp[0] = True

        # initialize first row (using only s2)
        for j in range(1, n + 1):
            dp[j] = dp[j - 1] and s2[j - 1] == s3[j - 1]

        for i in range(1, m + 1):
            # update dp[0] (using only s1)
            dp[0] = dp[0] and s1[i - 1] == s3[i - 1]

            for j in range(1, n + 1):
                k = i + j - 1

                take_s1 = dp[j] and s1[i - 1] == s3[k]
                take_s2 = dp[j - 1] and s2[j - 1] == s3[k]

                dp[j] = take_s1 or take_s2

        return dp[n]