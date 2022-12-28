from collections import deque


class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        n = len(s)
        if n < k:
            return 0

        size = 0
        window_set = set()
        window = deque()
        res = 0

        for i in range(n):
            if size == k:
                ch, _ = window.popleft()
                window_set.remove(ch)
                size -= 1

            if s[i] in window_set:
                while window[0][0] != s[i]:
                    ch, _ = window.popleft()
                    window_set.remove(ch)
                _, idx = window.popleft()
                size = i - idx - 1

            window_set.add(s[i])
            window.append((s[i], i))
            size += 1

            if size == k:
                res += 1

        return res
