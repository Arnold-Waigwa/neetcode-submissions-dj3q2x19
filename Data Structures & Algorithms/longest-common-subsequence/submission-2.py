class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        rows, cols = len(text1), len(text2)
        result = [[0] * cols for _ in range(rows)]

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                if text1[row] == text2[col]:
                    ans = result[row + 1][col + 1] if (row + 1 < rows and col + 1 < cols) else 0
                    result[row][col] = 1 + ans
                else:
                    r = result[row + 1][col] if row + 1 < rows else 0
                    c = result[row][col + 1] if col + 1 < cols else 0
                    result[row][col] = max(r, c)
        
        return result[0][0]

