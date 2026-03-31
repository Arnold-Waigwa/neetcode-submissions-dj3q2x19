class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #if we say starting from top left which is 0,0
        #check top, right, bottom, left for 1's
        #maintain a set to keep positions and avoid duplicate 1's
        #use dfs to go through each position
        #go through every position with a for loop
        count = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(i,j):
            if (
                i < 0 or j < 0 or i >= rows or j >= cols 
                or grid[i][j] == '0' or (i,j) in visited
            ):
                return False

            visited.add((i,j))

            top = dfs(i-1, j)
            right = dfs(i, j+1)
            bottom = dfs(i+1, j)
            left = dfs(i, j - 1)

            return True

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col):
                    count += 1

        return count



        