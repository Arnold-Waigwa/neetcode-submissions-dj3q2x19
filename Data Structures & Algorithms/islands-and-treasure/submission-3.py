class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visited = set()

        def addRoom(row, col):
            if (
                row < 0 or row >= rows or col < 0 or col >= cols
                or (row, col) in visited or grid[row][col] == -1
            ): return 

            q.append((row,col))
            visited.add((row, col))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    q.append((row, col))
                    visited.add((row, col))

        distance = 0
        while q:
            N = len(q)
            for _ in range(N):
                row, col = q.popleft()
                grid[row][col] = distance

                addRoom(row - 1, col)
                addRoom(row, col + 1)
                addRoom(row + 1, col)
                addRoom(row, col - 1)
            
            distance += 1





        