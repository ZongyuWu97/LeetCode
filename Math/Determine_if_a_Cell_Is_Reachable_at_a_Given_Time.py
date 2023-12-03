class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if sx == fx and sy == fy:
            return t >= 2 or t == 0
        count = t - max(abs(sx - fx), abs(sy - fy))
        return count >= 0 