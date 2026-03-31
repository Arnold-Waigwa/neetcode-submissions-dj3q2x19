class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Unpopulated hashmap to store character frequencies
        hashmap = {}
        l = 0  # Left pointer
        maxCount = 0  # Keep track of the count of the most frequent character
        maxSubstr = 0  # Longest valid substring length
        
        # Iterate over the string with the right pointer
        for r in range(len(s)):
            # Update the frequency of the current character
            hashmap[s[r]] = 1 + hashmap.get(s[r], 0)
            # Update the most frequent character count in the current window
            maxCount = max(maxCount, hashmap[s[r]])
            
            # If the number of characters we need to replace exceeds k, shrink the window
            if (r - l + 1) - maxCount > k:
                # Decrease the frequency of the left character and move the left pointer
                hashmap[s[l]] -= 1
                l += 1
            
            # Update the longest valid substring length
            maxSubstr = max(maxSubstr, r - l + 1)
        
        return maxSubstr

        
        