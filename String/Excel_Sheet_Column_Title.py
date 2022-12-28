class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        base = ord('A')
        res = []
        while columnNumber != 0:
            columnNumber, remainder = divmod(columnNumber - 1, 26)
            res.append(chr(base + remainder))
        return ''.join(res[::-1])
