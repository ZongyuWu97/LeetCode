import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        h = [intervals[0][1]]
        for interval in intervals[1:]:
            if interval[0] < h[0]:
                heapq.heappush(h, interval[1])
            else:
                heapq.heapreplace(h, interval[1])
        return len(h)
