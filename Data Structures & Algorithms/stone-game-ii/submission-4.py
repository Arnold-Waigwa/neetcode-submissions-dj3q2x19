class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] += suffix[i + 1] + piles[i]
        
        for i in range(n - 1, -1, -1):
            for M in range(n + 1):
                if i + 2 * M >= n:
                    dp[i][M] =  suffix[i]
                    continue
                best = 0
                for k in range(i, min(n, 2 * M + i)):
                    best = max(
                        best,
                        suffix[i] - dp[k + 1][max(k - i + 1, M)]
                    )
                dp[i][M] = best

        return dp[0][1]


            