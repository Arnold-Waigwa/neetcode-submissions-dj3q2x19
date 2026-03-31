class Solution:
    def isValid(self, s: str) -> bool:
        #have a hashmap that has key as open bracket and value as 
        #close bracket
        #Initialize a stack(pop or push)
        #iterate through the array :
        #   if it is open brackets, push onto stack
        #   if it is closed, checked if the closed bracket has a key
        #   as its corresponding value; if it does, pop it, if not, return false
        #   if gone throught the entire array and stack is empty, return true otherwise false

        bracketPair = {
            "]" : "[",
            ")" : "(",
            "}" : "{"
        }

        stack = []
        for v in s:
            if v == "{" or v == "(" or v == "[":
                stack.append(v)
            else:
                if stack:
                    if bracketPair[v] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        else:
            return True
            

        