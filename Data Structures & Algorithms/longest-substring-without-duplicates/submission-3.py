class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #have a left and right pointer
        #have a hashmap
        #while the right pointer's element doesn't exist
        #add it to the map
        #if it does exist, update max,remove the entry of left pointer
        #and update the left to left plus one
        l = longest = 0
        seen = {}
        for r in range(len(s)):
            while s[r] in seen:
                del seen[s[l]] 
                l += 1
            seen[s[r]] = 1
            longest = max(longest, r - l + 1)
        return longest
        
        