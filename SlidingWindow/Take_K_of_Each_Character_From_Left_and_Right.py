class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        n = len(s)
        na, nb, nc = 0, 0, 0
        for ch in s:
            if ch == 'a':
                na += 1
            elif ch == 'b':
                nb += 1
            else:
                nc += 1
        if any(nx < k for nx in [na, nb, nc]):
            return -1

        l, r, res = 0, 0, 0
        count = defaultdict(int)
        while r < n:
            count[s[r]] += 1
            while count['a'] > na - k or count['b'] > nb - k or count['c'] > nc - k:
                count[s[l]] -= 1
                l += 1
            r += 1
            res = max(res, r - l)
        return n - res
