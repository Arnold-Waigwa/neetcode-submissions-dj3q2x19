class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row, col))

        minutes = 0
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        while fresh and q:
            N = len(q)
            for _ in range(N):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (
                        nr in range(rows)
                        and nc in range(cols)
                        and grid[nr][nc] == 1 
                    ):
                        fresh -= 1
                        grid[nr][nc] = 2
                        q.append((nr, nc))
            minutes += 1

        return minutes if not fresh else -1



        