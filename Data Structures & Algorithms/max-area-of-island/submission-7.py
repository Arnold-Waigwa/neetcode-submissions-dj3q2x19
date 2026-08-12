class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        visited = set()
        def dfs(i, j):
            if (
                i < 0 or i >= rows or
                j < 0 or j >= cols or
                (i, j) in visited or
                grid[i][j] == 0
            ):
                return 0
            
            visited.add((i, j))
            ans = 1
            for dr, dc in neighbors:
                nr, nc = dr + i, dc + j
                ans += dfs(nr, nc)
            return ans


        res = 0
        for row in range(rows):
            for col in range(cols):
                res = max(res, dfs(row, col))
        
        return res