from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        freq_s1 = defaultdict(int)
        freq_s2 = defaultdict(int)

        for i in range(len(s1)):
            freq_s1[s1[i]] += 1
            freq_s2[s2[i]] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if freq_s1 == freq_s2:
                return True
            
            freq_s2[s2[r]] += 1
            freq_s2[s2[l]] -= 1

            if freq_s2[s2[l]] == 0:
                del freq_s2[s2[l]]

            l += 1


        return freq_s1 == freq_s2



        