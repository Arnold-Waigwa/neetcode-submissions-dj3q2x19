class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        cache = {}
        def dfs(a=1, b=1):
            if (a, b) in cache:
                return cache[(a, b)]
            if (a == m and b == n):
                return 1

            down = dfs(a + 1, b) if a < m else 0
            right = dfs(a, b + 1) if b < n else 0

            cache[(a, b)] = right + down
            return cache[(a, b)]
        
        return dfs()


