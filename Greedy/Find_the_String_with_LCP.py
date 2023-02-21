class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        res = [0] * n

        ch = 1
        for i in range(n):
            if res[i]:
                continue
            if ch > 26:
                return ''
            for j in range(i, n):
                if lcp[i][j]:
                    res[j] = ch
            ch += 1

        for i in range(n):
            for j in range(n):
                v = lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                v = v + 1 if res[i] == res[j] else 0
                if lcp[i][j] != v:
                    return ''

        return ''.join(chr(ord('a') + i - 1) for i in res)
