import heapq


class MedianFinder:

    def __init__(self):
        self.large_half_size = 0
        self.small_half_size = 0
        self.large_half = []
        self.small_half = []

    def addNum(self, num: int) -> None:
        if self.small_half_size == self.large_half_size:
            if not self.small_half or num <= self.large_half[0]:
                heapq.heappush(self.small_half, -num)
            else:
                heapq.heappush(self.large_half, num)
                heapq.heappush(self.small_half, -
                               heapq.heappop(self.large_half))
            self.small_half_size += 1

        else:
            if num >= -self.small_half[0]:
                heapq.heappush(self.large_half, num)
            else:
                heapq.heappush(self.small_half, -num)
                heapq.heappush(self.large_half, -
                               heapq.heappop(self.small_half))
            self.large_half_size += 1

    def findMedian(self) -> float:
        if self.small_half_size == self.large_half_size:
            return (-self.small_half[0] + self.large_half[0]) / 2
        else:
            return -self.small_half[0]
