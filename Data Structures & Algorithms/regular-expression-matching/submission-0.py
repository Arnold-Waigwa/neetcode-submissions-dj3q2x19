class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i: int, j: int) -> bool:
            if (i, j) in dp:
                return dp[(i, j)]

            # if pattern finished → must finish string too
            if j == len(p):
                return i == len(s)

            # check if current char matches
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            # handle *
            if j + 1 < len(p) and p[j + 1] == "*":
                # skip OR use star (only if match is possible)
                ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                ans = first_match and dfs(i + 1, j + 1)

            dp[(i, j)] = ans
            return ans

        return dfs(0, 0)