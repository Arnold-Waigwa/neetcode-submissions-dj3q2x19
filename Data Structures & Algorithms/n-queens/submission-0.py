class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        col_set = set()
        posDiag = set()
        negDiag = set()
        result = []
        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col_set or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                board[r][c] = "Q"
                col_set.add(c) 
                posDiag.add(r + c)
                negDiag.add(r - c)
                dfs(r+1)

                board[r][c] = "."
                col_set.remove(c) 
                posDiag.remove(r + c)
                negDiag.remove(r - c)
        dfs(0)
        return result


        