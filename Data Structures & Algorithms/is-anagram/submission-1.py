class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #first populate
        if len(s) != len(t): return False
        s_map, t_map = {}, {}
        for i in range(len(s)):
            s_map[s[i]] = s_map.get(s[i], 0) + 1
            t_map[t[i]] = t_map.get(t[i], 0) + 1

        #check if the keys match-up
        for k,v in t_map.items():
            if not t_map[k] == s_map.get(k):
                return False
        return True




        