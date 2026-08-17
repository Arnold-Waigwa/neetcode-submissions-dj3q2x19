class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        dfs(i) minimum left over char from i
        """
        dp = [0] * (len(s) + 1)

        for i in range(len(s) - 1, -1, -1):
            res = 1 + dp[i + 1]
            for word in dictionary:
                if s.startswith(word, i):
                    res = min(res, dp[i + len(word)])
            dp[i] = res
        
        return dp[0]

