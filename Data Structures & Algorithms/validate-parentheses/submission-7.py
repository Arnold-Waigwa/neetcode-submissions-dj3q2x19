class Solution:
    def isValid(self, s: str) -> bool:
        closed = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        for c in s:
            if c in closed:
                if not stack or stack[-1] != closed[c]:
                    return False
                stack.pop()
            else:
                stack.append(c)
                
        return not stack
