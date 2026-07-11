class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #a bfs solution: start at the edge, and check the neighbours
        #want to start at the top and go breadth first
        if not grid: return 0

        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        nr < 0 or nc < 0 or nr >= rows or nc >= cols
                        or (nr, nc) in visited or grid[nr][nc] == "0"
                    ):
                        continue
                    visited.add((nr, nc))
                    q.append((nr, nc))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1
        
        return islands
        