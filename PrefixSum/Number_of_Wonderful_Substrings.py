from collections import defaultdict


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        masks = defaultdict(int)
        masks[0] = 1
        binary = {}
        for i, ch in enumerate("abcdefghij"):
            binary[ch] = 1 << i

        res = 0
        curr_mask = 0
        for ch in word:
            curr_mask ^= binary[ch]
            res += masks[curr_mask]
            for i in range(10):
                res += masks[curr_mask ^ (1 << i)]
            masks[curr_mask] += 1
        return res
