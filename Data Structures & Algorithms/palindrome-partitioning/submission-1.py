class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(i, comb):
            if i == len(s):
                res.append(comb[:])
                return

            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    comb.append(s[i:j+1])
                    dfs(j+1, comb)
                    comb.pop()
            
        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left, right = left + 1, right - 1
            
            return True

        dfs(0, [])
        return res


            


        