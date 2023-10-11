class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        curr = 0
        operator = '+'
        stack = []
        for i in range(n):
            ch = s[i]
            if ch.isdigit():
                curr = curr * 10 + int(ch)
            if not ch.isdigit() and ch != ' ' or i == n - 1:
                if operator == '+':
                    stack.append(curr)
                elif operator == '-':
                    stack.append(-curr)
                elif operator == '*':
                    stack.append(stack.pop() * curr)
                elif operator == '/':
                    stack.append(int(stack.pop() / curr))
                operator = ch
                curr = 0
        return sum(stack)

