class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        path = set()  # holds visited (r, c) tuples in the current DFS path

        def dfs(r: int, c: int, i: int) -> bool:
            # 1) If we've matched all letters, success
            if i == len(word):
                return True

            # 2) If out of bounds, already used, or letter mismatch, fail
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                (r, c) in path or
                board[r][c] != word[i]):
                return False

            # 3) Mark this cell as used
            path.add((r, c))

            # 4) Recurse in all four directions for the next letter
            found = (dfs(r + 1, c, i + 1) or
                     dfs(r - 1, c, i + 1) or
                     dfs(r, c + 1, i + 1) or
                     dfs(r, c - 1, i + 1))

            # 5) Unmark (backtrack) before returning
            path.remove((r, c))
            return found

        # 6) Try starting the DFS from every cell
        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True

        return False
