class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits:
            return result
        
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",  # fixed here
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(combination, i):
            if len(combination) == len(digits):
                result.append(combination)
                return
            
            letters = digitToChar[digits[i]]  # fixed capitalization
            for ch in letters:
                dfs(combination + ch, i + 1)  # build new string

        dfs("", 0)
        return result