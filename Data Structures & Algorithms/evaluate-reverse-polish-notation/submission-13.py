class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = {
            "+" : lambda x, y: x + y,
            "-" : lambda x, y: x - y,
            "*" : lambda x, y: x * y,
            "/" : lambda x, y: int(x / y)
        }

        stack = []

        for token in tokens:
            if token in operands:
                b = stack.pop()
                a = stack.pop()
                stack.append(operands[token](a, b))
            else:
                stack.append(int(token))

        return stack[0]

