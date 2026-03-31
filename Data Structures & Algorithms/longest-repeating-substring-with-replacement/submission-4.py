class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashMap = {}
        maxCount = 0
        res = l = 0
        for r in range(len(s)):
            hashMap[s[r]] = hashMap.get(s[r], 0) + 1
            maxCount = max(maxCount, hashMap[s[r]] )
            length = r-l+1
            if  length - maxCount > k:
                hashMap[s[l]] -= 1
                l += 1
            else:
                res = max(res, length)
        return res
        
        