class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dfs(amt):
            if amt in memo:
                return memo[amt]
            if amt == 0:
                return 0
            if amt < 0:
                return float("inf")
            
            min_amt = float("inf")
            for i in range(len(coins)):
                min_amt = min(min_amt, dfs(amt - coins[i]))

            memo[amt] = min_amt + 1 
            return min_amt + 1

        ans = dfs(amount)
        return ans if ans < float("inf") else -1

            

            