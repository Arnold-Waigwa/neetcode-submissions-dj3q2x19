class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tSort = sorted(t)
        SSort = sorted(s)
        return tSort == SSort

        