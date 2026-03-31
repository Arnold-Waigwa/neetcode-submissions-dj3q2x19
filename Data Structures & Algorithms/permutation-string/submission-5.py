class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        #use array
        s1freq = [0] * 26
        s2freq = [0] * 26
        #every space correspond to letter
        for c in s1:
            s1freq[ord(c) - ord('a')] += 1

        for i in range(len(s1)):
            s2freq[ord(s2[i]) - ord('a')] += 1

        if s2freq == s1freq:
            return True

        l = 0
        for r in range(len(s1), len(s2)):
            s2freq[ord(s2[r]) - ord('a')] += 1
            s2freq[ord(s2[l]) - ord('a')] -= 1
            l += 1
            if s2freq == s1freq:
                return True
        return False



        