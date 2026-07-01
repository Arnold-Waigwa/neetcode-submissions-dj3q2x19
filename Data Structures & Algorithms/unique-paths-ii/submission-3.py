class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        recurrence for (i, j) = (i + 1, j) + (i, j + 1)
        for table, to calculate dp[i][j], dp[i - 1][j] + dp[i][j - 1]
        iteratively process every i,j. curr array will hold prev array
        values. 
        if a position is invalid(has 1), mark its dp pos a zero
        """
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0] * cols
        dp[0] = 0 if obstacleGrid[0][0] == 1 else 1
        #process first row

        for col in range(1, cols):
            #check if position is valid
            if obstacleGrid[0][col] == 1:
                dp[col] = 0
            else:
                dp[col] = dp[col - 1]
        
        #process rest of rows
        for row in range(1, rows):
            dp[0] = 0 if obstacleGrid[row][0] == 1 else dp[0]
            for col in range(1, cols):
                if obstacleGrid[row][col] == 1:
                    dp[col] = 0
                else:
                    dp[col] += dp[col - 1]
        
        return dp[-1]











