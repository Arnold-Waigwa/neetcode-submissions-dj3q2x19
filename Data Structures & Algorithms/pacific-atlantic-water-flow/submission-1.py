class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        rows, cols = len(heights), len(heights[0])
        what we know:
        pacific : row = 0 or col = 0
        atlantic : row = rows - 1 or col = cols - 1
        """
        rows, cols = len(heights), len(heights[0])
        pacific_set, atlantic_set = set(), set()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific_set.add((row, col))
        for row in range(rows):
            for col in range(cols):
                if row == rows - 1 or col == cols - 1:
                    atlantic_set.add((row, col))

        def pacificDfs(row, col):
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    nr < 0 or nr >= rows or nc < 0 or nc >= cols
                    or (nr, nc) in pacific_set 
                    or heights[nr][nc] < heights[row][col]  
                ): continue
                pacific_set.add((nr, nc))
                pacificDfs(nr, nc)
            return

        def atlanticDfs(row, col):
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if (
                    nr < 0 or nr >= rows or nc < 0 or nc >= cols
                    or (nr, nc) in atlantic_set 
                    or heights[nr][nc] < heights[row][col]  
                ): continue
                atlantic_set.add((nr, nc))
                atlanticDfs(nr, nc)
            return

        for row, col in list(pacific_set):
            pacificDfs(row, col)
        for row, col in list(atlantic_set):
            atlanticDfs(row, col)

        res = []
        for item in pacific_set:
            if item in atlantic_set:
                res.append(list(item))  

        return res
