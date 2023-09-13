class Solution:
    def countOrders(self, n: int) -> int:
        res = 1
        MOD = 10 ** 9 + 7
        for i in range(2, n + 1):
            res *= i * (2 * i - 1)
            res %= MOD
        return res