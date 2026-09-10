class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #frequency of target
        t_count = {}
        for c in t:
            t_count[c] = 1 + t_count.get(c, 0)
        
        min_string = ""
        min_length = float("inf")
        have = 0
        need = len(t_count)

        l = 0
        for r in range(len(s)):
            if s[r] in t_count:
                t_count[s[r]] -= 1
                if t_count[s[r]] == 0:
                    have += 1
                
            while have == need:
                if r - l + 1 < min_length:
                    min_length = r - l + 1
                    min_string = s[l : r + 1]
                
                if s[l] in t_count:
                    t_count[s[l]] += 1
                    if t_count[s[l]] > 0:
                        have -= 1
                
                l += 1
        
        return min_string 


                

                
            



