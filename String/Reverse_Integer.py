class Solution:
    def reverse(self, x: int) -> int:
        MAX = str(2 ** 31)
        ansLst = reversed(list(str(abs(x))))
        ansStr = ''.join(ansLst).rjust(10)
        if ansStr > MAX:
            return 0
        return int(ansStr) * (1 - 2 * (x < 0))

