class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        digit_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",  
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def dfs(i, curr):
            if len(curr) == len(digits):
                res.append(curr)
                return
            
            letters = digit_to_letters[digits[i]]
            for letter in letters:
                dfs(i+1, curr + letter)

        dfs(0, "")
        return res