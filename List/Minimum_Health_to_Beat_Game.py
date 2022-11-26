class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        return sum(damage) + 1 - min(armor, max(damage))
