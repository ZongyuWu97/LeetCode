class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0
        l = 1
        r = x // 2
        while l < r:
            mid = (l + r + 1) // 2
            if mid * mid <= x:
                l = mid
            else:
                r = mid - 1
        return l
