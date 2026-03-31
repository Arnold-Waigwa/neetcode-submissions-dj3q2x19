from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #multisource bfs starting from the treasures
        #enqueue all the treasure locations
        #initialize a counter at 1
        #while q
        #popleft and set valid neighbors to the counter, enquiing them 
        #proceed until queue is empty and return the grid
        rows, cols = len(grid), len(grid[0])
        q = deque()
        inf = 2147483647
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
        
        counter = 1
        while q:
            length = len(q)
            for i in range(length):
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (
                        0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == inf
                    ):
                        grid[nr][nc] = counter
                        q.append((nr, nc))
            counter += 1
        
        





        