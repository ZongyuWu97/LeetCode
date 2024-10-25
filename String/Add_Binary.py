class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = max(len(a), len(b))
        a, b = a.zfill(n), b.zfill(n)
        carry = 0
        res = []
        for i in range(n - 1, -1, -1):
            carry += int(a[i] == "1") + int(b[i] == "1")
            res.append(str(carry % 2))
            carry //= 2

        if carry == 1:
            res.append("1")
        return "".join(reversed(res))
