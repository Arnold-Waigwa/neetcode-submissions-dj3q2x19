class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        # dp[i][j] = whether s[:i] matches p[:j]
        dp = [[False] * (m + 1) for _ in range(n + 1)]

        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(2, m + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2]

        for i in range(1, n + 1):
            for j in range(1, m + 1):

                if p[j - 1] != "*":
                    first_match = (
                        p[j - 1] == s[i - 1]
                        or p[j - 1] == "."
                    )

                    dp[i][j] = (
                        first_match
                        and dp[i - 1][j - 1]
                    )

                else:
                    # Option 1: use zero occurrences
                    dp[i][j] = dp[i][j - 2]

                    # Option 2: use one or more occurrences
                    first_match = (
                        p[j - 2] == s[i - 1]
                        or p[j - 2] == "."
                    )

                    if first_match:
                        dp[i][j] |= dp[i - 1][j]

        return dp[n][m]