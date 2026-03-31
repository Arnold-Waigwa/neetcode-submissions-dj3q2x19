class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #bfs approach
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        rows, cols = len(grid), len(grid[0])
        visited = set()
        max_area = 0

        def bfs(row, col):
            area = 1
            q = deque()
            q.append((row, col))
            visited.add((row, col))
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        0 <= nr < rows and 0 <= nc < cols
                        and grid[nr][nc] == 1 
                        and (nr, nc) not in visited
                    ):
                        visited.add((nr, nc))
                        q.append((nr, nc))
                        area += 1
            return area

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row, col) not in visited:
                    max_area = max(max_area, bfs(row, col))

        return max_area