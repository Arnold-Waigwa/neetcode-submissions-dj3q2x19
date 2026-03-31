class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #1,2 +
        #pop both of them and add them
        #3,3, *
        #9,4, -
        #5
        stack = []
        operators = {
            "+": 1,
            "-": 1,
            "*": 1,
            "/": 1,
        }
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                if s == "+":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    num3 = num1 + num2
                    stack.append(num3)
                elif s == "-":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    num3 = num1 - num2
                    stack.append(num3)
                elif s == "*":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    num3 = num1 * num2
                    stack.append(num3)
                elif s == "/":
                    num2 = stack.pop()
                    num1 = stack.pop()
                    num3 = int(num1/num2)
                    stack.append(num3)
        return stack[-1]