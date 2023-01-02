class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        while s:
            idx = s.index(s[-1])
            if idx == len(s) - 1:
                res += idx // 2
            else:
                res += idx
                s.pop(idx)
            s.pop()
        return res
