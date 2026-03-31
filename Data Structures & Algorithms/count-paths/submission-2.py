class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #initialize 2d array
        #store states in a 2d array starting from the bottom right
        #use a loop to process each cell with the formula
        #each cell = right cell if inboud else 0 + down cell inbound else 0
        #return top cell

        result = [[1] * n for _ in range(m)]

        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row == m - 1 and col == n - 1:
                    continue
                right = result[row][col + 1] if col < n - 1 else 0
                down = result[row + 1][col] if row < m - 1 else 0
                result[row][col] = right + down
        
        return result[0][0]