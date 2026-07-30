from functools import cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n = total // 2
        @cache
        def dfs(i, amt):
            if amt > n:
                return float("-inf")
            
            if i == len(stones):
                return amt
            
            return max(
                dfs(i + 1, amt),
                dfs(i + 1, amt + stones[i])
            )
        best = dfs(0, 0)
        other = total - best
        return abs(best - other)
        