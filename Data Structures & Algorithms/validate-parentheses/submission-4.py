class Solution:
    def isValid(self, s: str) -> bool:
        #if its an open bracket, push it
        #if its a closing bracket, make sure if matches top
        #of stack bracket pop it. If we reached end of 
        #s and have empty stack,, then its valid. If we reach
        #end and have not empty stack, not valid
        valid = { ")" : "(", "]" : "[", "}" : "{" }
        stack = [] 

        for c in s:
            if c not in valid: stack.append(c)
            else:
                if stack and valid[c] == stack[-1]:
                    stack.pop()
                else: return False

        return not stack 


        