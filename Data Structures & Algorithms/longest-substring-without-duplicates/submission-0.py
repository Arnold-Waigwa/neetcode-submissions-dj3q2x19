class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l += 1
            store.add(s[r])
            res = max(res, r - l + 1)
        return res

        