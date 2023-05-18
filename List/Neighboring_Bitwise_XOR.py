class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        prev = first = False
        for bit in derived:
            if bit:
                prev = not prev
        return prev == first
                