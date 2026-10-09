from functools import cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        n = total // 2

        @cache
        def dfs(i, num):
            if num > n:
                return float("-inf")

            if i >= len(stones):
                return num
            
            return max(
                dfs(i + 1, num + stones[i]),
                dfs(i + 1, num)
            )
        
        first = dfs(0, 0)
        second = total - first
        
        return second - first



            
            

