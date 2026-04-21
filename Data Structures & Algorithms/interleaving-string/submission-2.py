class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = {}
        
        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            k = i + j
            if k == len(s3):
                return True
            
            word = s3[k]

            left = False
            right = False

            if i < len(s1) and word == s1[i]:
                left = dfs(i + 1, j)

            if j < len(s2) and word == s2[j]:
                right = dfs(i, j + 1)


            dp[(i, j)] = left or right
            return dp[(i, j)]
        
        return dfs(0, 0)