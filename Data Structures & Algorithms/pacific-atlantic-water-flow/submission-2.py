class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #dfs starting from the oceans with reverse logic
        rows, cols = len(heights), len(heights[0])
        pacific_set, atlantic_set = set(), set()
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

        for row in range(rows):
            for col in range(cols):
                if row == 0 or col == 0:
                    pacific_set.add((row, col))
                if row == rows - 1 or col == cols - 1:
                    atlantic_set.add((row, col)) 
        
        def pacificDfs(row, col):
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if (
                    0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in pacific_set and
                    heights[nr][nc] >= heights[row][col]
                ):
                    pacific_set.add((nr, nc))
                    pacificDfs(nr, nc)
        
        def atlanticDfs(row, col):
            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                if (
                    0 <= nr < rows and 0 <= nc < cols and
                    (nr, nc) not in atlantic_set and
                    heights[nr][nc] >= heights[row][col]
                ):
                    atlantic_set.add((nr, nc))
                    atlanticDfs(nr, nc)
        
        #run dfs from every position in the set and access whether it can reach current location
        for row, col in list(pacific_set):
            pacificDfs(row, col)
        
        for row, col in list(atlantic_set):
            atlanticDfs(row, col)

        res = []
        for (row, col) in pacific_set:
            if (row, col) in atlantic_set:
                res.append([row, col])
        
        return res
        

        