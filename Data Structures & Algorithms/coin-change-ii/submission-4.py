class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        # Base case
        for i in range(len(coins) + 1):
            dp[i][0] = 1  # one way to make 0 (use nothing)

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                dp[i][j] = dp[i - 1][j]  # skip coin
                
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]  # take coin

        return dp[len(coins)][amount]