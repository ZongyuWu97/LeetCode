class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        zeros = []
        ones = []
        prev = s[0]
        idx = 0
        cnt = 1
        
        for i in range(1, len(s)):
            ch = s[i]
            if ch == prev:
                cnt += 1
            else:
                if prev == '0':
                    zeros.append((idx, cnt))
                else:
                    ones.append((idx, cnt))
                prev = ch
                cnt = 1
                idx = i

        if prev == '0':
            zeros.append((idx, cnt))
        else:
            ones.append((idx, cnt))
        res = 0

        for idx, length in zeros:
            for pair in ones:
                if idx + length == pair[0]:
                    res = max(res, 2 * min(length, pair[1]))
        return res