from collections import defaultdict, Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = defaultdict(int)
        count = Counter(t)
        enough = 0
        n = len(s)
        l = len(count)
        i, j = 0, 0
        min_length = float("inf")
        res = ""
        while j < n:
            ch = s[j]
            window[ch] += 1
            if ch in count and window[ch] == count[ch]:
                enough += 1
            if enough == l:
                while enough == l:
                    window[s[i]] -= 1
                    if s[i] in count and window[s[i]] == count[s[i]] - 1:
                        enough -= 1
                    i += 1
                if j - i + 2 < min_length:
                    min_length = j - i + 2
                    res = s[i - 1 : j + 1]
            j += 1
        return res
