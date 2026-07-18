import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])
        # effort[r][c] = minimum effort needed to reach (r, c)
        effort = [[float("inf")] * cols for _ in range(rows)]
        effort[0][0] = 0
        pq = [(0, 0, 0)]  # (current_effort, row, col)
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while pq:
            curr_effort, r, c = heapq.heappop(pq)
            if (r, c) == (rows - 1, cols - 1):
                return curr_effort
            # Ignore outdated entries
            if curr_effort > effort[r][c]:
                continue
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    edge_cost = abs(heights[r][c] - heights[nr][nc])
                    new_effort = max(curr_effort, edge_cost)

                    if new_effort < effort[nr][nc]:
                        effort[nr][nc] = new_effort
                        heapq.heappush(pq, (new_effort, nr, nc))
