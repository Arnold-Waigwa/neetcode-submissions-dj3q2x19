class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #you can have a sliding window and set
        #hashset
        hashset = set()
        count = 0
        l = 0
        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            count = max(count, r - l + 1)
        return count
            




  





        
        