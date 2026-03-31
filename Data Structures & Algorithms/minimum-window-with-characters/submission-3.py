class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #verify length
        if len(t) > len(s): return ""

        #change t into hashmap
        tmap = {}
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)

        seen = len(t)
        l, output = 0, []
        for r in range(len(s)):
            if s[r] in tmap:
                if tmap[s[r]] > 0:
                    seen -= 1
                tmap[s[r]] -= 1

            while seen == 0:
                length = r - l + 1
                output.append((length, s[l:r+1]))
                if s[l] in tmap:
                    tmap[s[l]] += 1
                    if tmap[s[l]] > 0:
                        seen += 1
                l += 1
        if output:
            min_tuple = min(output, key=lambda x: x[0])
            return min_tuple[1]
        else:
            return ""





        