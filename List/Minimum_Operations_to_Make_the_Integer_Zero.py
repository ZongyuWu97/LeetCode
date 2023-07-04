
class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        for k in range(1, 61):
            if (num1 - k * num2).bit_count() <= k <= num1 - k * num2:
                return k
        return -1