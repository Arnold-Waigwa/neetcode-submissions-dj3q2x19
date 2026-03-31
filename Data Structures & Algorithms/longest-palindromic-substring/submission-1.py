class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = []
        n = len(s)
        for i in range(n):
            l, r = i, i
            while (l >= 0 and r < n) and s[l] == s[r]:
                if not res:
                    res.append(s[l:r+1])
                elif len(s[l:r+1]) > len(res[0]):
                    res[0] = s[l:r+1]
                l, r = l - 1, r + 1
            
            l, r = i, i + 1
            while (l >= 0 and r < n) and s[l] == s[r]:
                if not res:
                    res.append(s[l:r+1])
                elif len(s[l:r+1]) > len(res[0]):
                    res[0] = s[l:r+1]
                l, r = l - 1, r + 1

        return res[0]
        