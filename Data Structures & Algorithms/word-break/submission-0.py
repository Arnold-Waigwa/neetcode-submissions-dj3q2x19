class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo: return memo[i]
            if i >= len(s):
                memo[i] = 1
                return True
            for word in wordDict:
                if word != s[i: i + len(word)]:
                    continue
                if dfs(i + len(word)):
                    return True
            memo[i] = 0
            return False

        return dfs(0)
            