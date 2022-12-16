class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_hour = hour * 30 + minutes / 60 * 30
        angle_minutes = minutes / 60 * 360
        angle = abs(angle_hour - angle_minutes)
        return min(angle, abs(360 - angle))
