class Solution:
    def maxScore(self, s: str) -> int:
        n, res = len(s), 0
        for i in range(1, n):
            left_zero = 0
            for j in range(i):
                if s[j] == '0':
                    left_zero += 1
            right_one = 0
            for j in range(i, n):
                if s[j] == '1':
                    right_one += 1
            res = max(res, left_zero + right_one)
        return res