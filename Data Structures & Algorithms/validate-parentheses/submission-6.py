class Solution:
    def isValid(self, s: str) -> bool:
        #input string
        para_map = {
            "}":"{",
            ")":"(",
            "]":"[",
        }

        stack = []
        for string in s:
            if string not in para_map:
                stack.append(string)
            else:
                if not stack or para_map[string] != stack[-1]:
                    return False
                stack.pop()

        return len(stack) == 0
        