class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        result = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(result)):
            result[i][amount] = 1

        for i in range(len(coins) - 1, -1, -1):
            for j in range(amount - 1, -1, -1):
                take = result[i][j + coins[i]] if j + coins[i] <= amount else 0
                keep = result[i + 1][j]
                result[i][j] = take + keep
        
        return result[0][0]