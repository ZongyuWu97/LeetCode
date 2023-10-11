class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            elif ch == '+':
                res += sign * operand
                operand = 0
                sign = 1
            elif ch == '-':
                res += sign * operand
                operand = 0
                sign = -1
            elif ch == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif ch == ')':
                res += sign * operand
                res *= stack.pop()
                res += stack.pop()
                operand = 0
        return res + sign * operand