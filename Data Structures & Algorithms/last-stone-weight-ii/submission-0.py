from functools import lru_cache

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = total // 2

        @lru_cache(None)
        def dfs(i, curr_sum):
            if curr_sum > target:
                return -float("inf")     

            if i == len(stones):
                return curr_sum

            return max(
                dfs(i + 1, curr_sum + stones[i]), 
                dfs(i + 1, curr_sum)               
            )
            
        best = dfs(0, 0)
        return total - 2 * best
