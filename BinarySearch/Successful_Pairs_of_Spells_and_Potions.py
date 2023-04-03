class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        n = len(potions)
        for spell in spells:
            res.append(n - bisect.bisect_left(potions, math.ceil(success / spell)))
        return res