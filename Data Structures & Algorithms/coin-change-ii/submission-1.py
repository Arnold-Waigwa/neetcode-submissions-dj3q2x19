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
            
            cache[(i, amt)] = dfs(i, amt + coins[i]) + dfs(i + 1, amt)
            return cache[(i, amt)]
        
        return dfs(0, 0)