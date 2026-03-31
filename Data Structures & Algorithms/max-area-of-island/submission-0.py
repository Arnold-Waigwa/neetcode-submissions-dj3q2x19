class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #dfs approach
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def dfs(row, col):
            if (
                row < 0 or row >= rows or col < 0 or col >= cols
                or (row, col) in visited or grid[row][col] == 0
            ):
                return 0

            visited.add((row, col))
            top = dfs(row - 1, col)
            right = dfs(row, col + 1)
            bottom = dfs(row + 1, col)
            left = dfs(row, col - 1)

            return 1 + top + right + bottom + left
            

        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, dfs(row, col))
        
        return max_area