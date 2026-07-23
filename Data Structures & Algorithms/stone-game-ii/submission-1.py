class Solution:
    def stoneGameII(self, piles: List[int]) -> int:  
        """
        """
        n = len(piles)
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] += suffix[i + 1] + piles[i]
        
        dp = {}
        
        def dfs(i, M):
            if (i, M) in dp:
                return dp[(i, M)]
            
            if i + 2 * M >= n:
                return suffix[i]

            if i >= n:
                return 0
            
            dp[(i, M)] = 0
            for j in range(i, min(i + 2 * M , n)):
                dp[(i, M)] = max(
                    dp[(i, M)],
                    suffix[i] - dfs(j + 1, max(j - i + 1, M))
                )
            
            return dp[(i, M)]
        
        return dfs(0, 1)
                



