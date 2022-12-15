class Solution:
    def minSwaps(self, s: str) -> int:
        def countDiff(b):
            cnt = 0
            for i in range(0, n, 2):
                if s[i] != b:
                    cnt += 1
            return cnt

        n = len(s)
        n0 = s.count('0')
        n1 = s.count('1')
        diff = n0 - n1
        if abs(diff) > 1:
            return -1
        elif diff == 1:
            return countDiff('0')
        elif diff == -1:
            return countDiff('1')
        else:
            return min(countDiff('0'), countDiff('1'))
