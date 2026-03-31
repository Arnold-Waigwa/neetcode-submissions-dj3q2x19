class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        #how would we do a dfs?
        #dimensions of pacific = first row, first col
        # heights[0] for row in rows, for col in cols, if cols = 0, in pacific
        #if row = 0, in pacific
        #atlantic = last row, last col = heights[len(heights)], 
        #[0,0] up, right, down, left
        #impose a check, are you in pacific? row == 0? are you atlantic?
        rows, cols = len(heights), len(heights[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        res = []

        def bfs(row, col, pacific=False, atlantic=False):
            visited = set()
            q = deque()
            q.append((row, col))
            while q:
                row, col = q.popleft()
                visited.add((row, col))
                if pacific or row == 0 or col == 0:
                    pacific = True
                if atlantic or row == rows - 1 or col == cols - 1:
                    atlantic = True
                if pacific and atlantic:
                    return True 
                
                for dr, dc in directions:
                    nrow, ncol = row + dr, col + dc
                    if (
                        nrow in range(rows) and ncol in range(cols)
                        and heights[nrow][ncol] <= heights[row][col]
                        and (nrow, ncol) not in visited
                    ):
                        q.append((nrow, ncol))
            return False


        for row in range(rows):
            for col in range(cols):
                if bfs(row, col):
                    res.append([row, col])

        return res
                    

        