class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alNum(c):
            return ('a' <= c <= 'z') or c.isdigit()

        l, r = 0, len(s) - 1
        s = s.lower()

        while l < r:
            while l < r and not alNum(s[l]):
                l += 1
            while l < r and not alNum(s[r]):
                r -= 1
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1

        return True
