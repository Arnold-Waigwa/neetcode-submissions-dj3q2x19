from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        rows, cols = len(grid), len(grid[0])

        visited = set()
        q = deque()
        def bfs(i, j):
            q.append((i, j))
            ans = 0

            while q:
                r, c = q.pop()
                if (
                    r < 0 or r >= rows or
                    c < 0 or c >= cols or
                    (r, c) in visited or
                    grid[r][c] == 0
                ):
                    continue

                visited.add((r, c))
                ans += 1
                for dr, dc in neighbors:
                    q.append((r + dr, c + dc))

            return ans
        
        res = 0
        for row in range(rows):
            for col in range(cols):
                res = max(res, bfs(row, col))
        
        return res