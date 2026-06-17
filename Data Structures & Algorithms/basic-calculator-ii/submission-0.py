class Solution:
    def calculate(self, s: str) -> int:
        total = prev = num = 0
        op = '+'
        n = len(s)
        i = 0

        while i <= n:
            ch = s[i] if i < n else '+'
            if ch == ' ':
                i += 1
                continue

            if '0' <= ch <= '9':
                num = num * 10 + (ord(ch) - ord('0'))
            else:
                if op == '+':
                    total += prev
                    prev = num
                elif op == '-':
                    total += prev
                    prev = -num
                elif op == '*':
                    prev = prev * num
                else:
                    if prev < 0:
                        prev = -(-prev // num)
                    else:
                        prev = prev // num

                op = ch
                num = 0

            i += 1

        total += prev
        return total