import heapq


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        h = []
        time = 0
        for duration, lastDay in courses:
            if time + duration <= lastDay:
                heapq.heappush(h, -duration)
                time += duration
            elif h and duration < -h[0]:
                time = time + h[0] + duration
                heapq.heapreplace(h, -duration)
        return len(h)
