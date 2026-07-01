class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        recurrence (i, j) = grid[i][j] + min((i + 1, j), (i, j + 1))
        only need value of prev table
        """
        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols

        dp[0] = grid[0][0]

        for col in range(1, cols):
            dp[col] = grid[0][col] + dp[col - 1]
        
        for row in range(1, rows):
            dp[0] += grid[row][0]
            for col in range(1, cols):
                dp[col] = grid[row][col] + min(dp[col], dp[col - 1])
        
        return dp[-1]