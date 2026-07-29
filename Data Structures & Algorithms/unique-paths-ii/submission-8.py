class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 1 if obstacleGrid[0][0] == 0 else 0

        for col in range(1, cols):
            if obstacleGrid[0][col] == 1:
                dp[col] = 0
            else:
                dp[col] = dp[col - 1]
        
        for row in range(1, rows):
            dp[0] = 0 if obstacleGrid[row][0] == 1 else dp[0]
            for col in range(1, cols):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                else:
                    dp[col] += dp[col - 1]
        
        return dp[-1]