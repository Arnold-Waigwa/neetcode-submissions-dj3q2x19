class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
	        return ""
        
        #initialize the dictionaries
        dictionary = {}
        for c in t:
            dictionary[c] = 1 + dictionary.get(c, 0)

        required = len(t)
        substrings = []
        l = r = 0

        while r < len(s):
            if s[r] in dictionary:
                if dictionary[s[r]] > 0:
                    required -= 1
                dictionary[s[r]] -= 1
                
            while required == 0:
                length = r - l + 1
                substrings.append((length, s[l:r+1]))

                if s[l] in dictionary:
                    dictionary[s[l]] += 1
                    if dictionary[s[l]] > 0:
                        required += 1

                l += 1
            r += 1
        
        if substrings:
            min_tuple = min(substrings, key=lambda x: x[0])
            return min_tuple[1]
        else:
            return ""

        
                    





