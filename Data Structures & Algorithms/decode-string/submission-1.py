class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c == "]":
                curr = []

                while stack and stack[-1] != "[":
                    curr.append(stack.pop())

                stack.pop()  # Remove [

                curr.reverse()
                num = []

                while stack and stack[-1].isdigit():
                    num.append(stack.pop())

                count = int("".join(reversed(num)))

                stack.append("".join(curr) * count)

            else:
                stack.append(c)

        return "".join(stack)