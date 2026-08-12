class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        neighbors = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        def dfs(i, j, k):
            if k == len(word):
                return True
            if (
                i < 0 or i >= rows or
                j < 0 or j >= cols or
                (i, j) in visited or
                board[i][j] != word[k]
            ):
                return False
            
            res = False
            visited.add((i, j))
            for dr, dc in neighbors:
                nr, nc = dr + i, dc + j
                res |= dfs(nr, nc, k + 1)

            visited.remove((i, j))
            return res

        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False
        