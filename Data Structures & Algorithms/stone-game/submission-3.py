from functools import lru_cache
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def dfs(i, j) -> int:
            if i == j:
                return piles[i]
            #take max advantage
            return max(
                piles[i] - dfs(i + 1, j),
                piles[j] - dfs(i, j - 1)
            )
        
        return dfs(0, (len(piles) - 1)) > 0