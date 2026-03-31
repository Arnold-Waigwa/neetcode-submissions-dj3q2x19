class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # Frequency map for characters in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # Left and right pointers
        l, r = 0, 0
        # Number of characters from t we need to match
        required = len(t)
        substrings = []
        
        while r < len(s):
            # If the character at r is in t, decrease its required count
            if s[r] in t_count:
                if t_count[s[r]] > 0:
                    required -= 1
                t_count[s[r]] -= 1
            
            # When all characters are matched
            while required == 0:
                substr_length = r - l + 1
                substrings.append((substr_length, s[l:r+1]))
                
                # Try to move the left pointer to reduce the window size
                if s[l] in t_count:
                    t_count[s[l]] += 1
                    if t_count[s[l]] > 0:
                        required += 1
                
                l += 1
            
            r += 1
        
        if substrings:
            min_tuple = min(substrings, key=lambda x: x[0])
            return min_tuple[1]
        return ""
