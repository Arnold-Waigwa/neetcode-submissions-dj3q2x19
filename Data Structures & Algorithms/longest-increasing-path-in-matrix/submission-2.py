class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows, cols = len(matrix), len(matrix[0])

        dp = {} #store our answers

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]
            
            ans = float("-inf")
            for dr, dc in directions:
                nr, nc = i + dr, j + dc
                #check for validity
                if (
                    0 <= nr < rows and 0 <= nc < cols and
                    matrix[nr][nc] > matrix[i][j] 
                ):
                    ans = max(ans, dfs(nr, nc))

            #base case
            if ans == float("-inf"):
                return 1
            
            #otherwise, store the ans + 1 and return it
            dp[(i, j)] = 1 + ans
            return dp[(i, j)]
        

        #go through every position and find the best answer
        res = float("-inf")
        for row in range(rows):
            for col in range(cols):
                res = max(res, dfs(row, col))
        
        return res