class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)

        def helper(matrix):
            res = 0
            for i in range(n):
                for j in range(n):
                    if i == j:
                        res += matrix[i][j]
                matrix[i].reverse()
            return res

        return helper(mat) + helper(mat) - (mat[n // 2][n // 2] if n & 1 else 0)