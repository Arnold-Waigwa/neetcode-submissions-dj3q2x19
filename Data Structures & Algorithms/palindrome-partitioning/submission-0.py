class Solution:
    def partition(self, s: str) -> List[List[str]]:
        part = []
        result = []
        def dfs(i):
            if i >= len(s):
                result.append(part.copy())
                return
            for j in range(i, len(s)):
                if isPali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True
        dfs(0)
        return result
        