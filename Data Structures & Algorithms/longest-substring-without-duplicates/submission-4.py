class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #have a left and right pointer
        #have a hashmap
        #while the right pointer's element doesn't exist
        #add it to the map
        #if it does exist, update max,remove the entry of left pointer
        #and update the left to left plus one
        seen = set()
        l = 0
        largest = 0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            largest = max(largest, r - l + 1)
        return largest
        
        
        