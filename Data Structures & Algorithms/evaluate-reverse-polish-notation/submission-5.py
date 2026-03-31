class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #initialize a stack
        #go through every string and push it onto the stack while
        #converted as an integer
        #if met with an operand, pop the previous two values,
        # and evaluate them and push the result
        #go on until the end of the list
        stack = []
        for val in tokens:
            #if its not an operand push it
            if val != '+' and val != '-' and val != '*' and val != '/':
                stack.append(val)
            else:
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                if val == '+':
                    val3 = val1 + val2
                    stack.append(val3)
                elif val == '-':
                    val3 = val1 - val2
                    stack.append(val3)
                elif val == '*':
                    val3 = val1 * val2
                    stack.append(val3)
                elif val == '/':
                    val3 = val1 / val2
                    stack.append(val3)
        return int(stack[0])
                


        
