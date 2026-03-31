class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #valid if (window length - most common) <= k
        #how to keep track of most common
        l = longest = 0
        freq = {}
        for r in range(len(s)):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            while (r - l + 1) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
        return longest
        


        