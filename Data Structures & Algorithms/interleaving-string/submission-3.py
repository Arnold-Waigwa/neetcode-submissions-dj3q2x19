class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        M, N, P = len(s1), len(s2), len(s3)
        if M + N != P:
            return False
        

        dp = [[False] * (N + 1) for _ in range(M + 1)]

        dp[M][N] = True

        for i in range(M, -1, -1):
            for j in range(N, -1, -1):
                k = i + j
                if k == P:
                    continue
                right = dp[i + 1][j] and s3[k] == s1[i] if i < M else False
                left = dp[i][j + 1] and s3[k] == s2[j] if j < N else False
                dp[i][j] = right or left

        
        return dp[0][0]