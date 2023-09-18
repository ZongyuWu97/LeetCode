class Solution:
    def findNthDigit(self, n: int) -> int:
        digit = 1
        cnt = 9
        st = 1
        while cnt*digit < n:
            n -= cnt*digit
            digit += 1
            cnt *= 10
            st *= 10

        st += (n- 1)/digit
        st = str(st)
        return int(st[(n-1)%digit])