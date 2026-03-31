class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0
        def dfs(num):
            nonlocal res
            if num == n:
                res += 1
                return
            if num > n:
                return 
            dfs(num + 1)
            dfs(num + 2)
            return
        
        dfs(0)
        return res
                

        