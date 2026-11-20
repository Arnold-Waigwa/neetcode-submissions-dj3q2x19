from functools import cache
class Solution:
    def integerBreak(self, n: int) -> int:
        """

        n = 4
        (n) for i in range(i, n)
            4 - 1
            4 - 2, 2  
            4 - 3
            4 - 4 return 1
        """
        @cache
        def dfs(n):
            if n == 1:
                return 1
            
            res = 0
            for i in range(1, n):
                res = max(res, i * (n - i), i * dfs(n - i))
            
            return res
        
        return dfs(n)












