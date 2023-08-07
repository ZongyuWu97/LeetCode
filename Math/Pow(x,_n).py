import sys
class Solution:
    def myPow(self, x: float, n: int) -> float:
        powers = x
        check = 0
        # powers
        res = 1
        absN = abs(n)
        LIMIT = math.sqrt(sys.float_info.max)
        while (1 << check) <= absN:
            
            if (1 << check) & absN:
                res *= powers
            check += 1
            print(check)
            if powers > LIMIT:
                return 0
            powers **= 2
            # print(res)
        return 1 / res if n < 0 else res