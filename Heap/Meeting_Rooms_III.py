import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        available = list(range(n))
        busy = []
        usage = [0] * n
        delay = 0
        meetings.sort()

        for meeting in meetings:
            start = meeting[0]
            end = meeting[1]
            while busy and busy[0][0] <= start:
                heapq.heappush(available, heapq.heappop(busy)[1])

            if available:
                room = heapq.heappop(available)
                heapq.heappush(busy, (end, room))
                usage[room] += 1
            else:
                delay = busy[0][0] - start
                usage[busy[0][1]] += 1
                heapq.heapreplace(busy, (end + delay, busy[0][1]))
            # print(busy, usage)
        return usage.index(max(usage))
