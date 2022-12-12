class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        prev = 0
        for interval in intervals:
            if interval[0] < prev:
                return False
            prev = interval[1]
        return True
