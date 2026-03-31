class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        
        def dfs(i, amt):
            if i == len(coins) or amt > amount:
                return 0
            
            if (i, amt) in cache:
                return cache[(i, amt)]
            
            if amt == amount:
                return 1
            
            ans = 0
            for j in range(i, len(coins)):
                ans += dfs(j, amt + coins[j])
            
            cache[(i, amt)] = ans
            return ans
        
        return dfs(0, 0)