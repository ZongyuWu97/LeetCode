class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist) - 1 >= hour:
            return -1
        left, right = 1, 10 ** 7

        def verify(speed):
            total = 0
            for d in dist[:-1]:
                # print(d / speed)
                total += math.ceil(d / speed)
                # print(total)
            total += dist[-1] / speed
            # print(total)
            return total <= hour

        while left < right:
            mid = (left + right) // 2
            # print(left, right, mid)
            if verify(mid):
                right = mid
            else:
                left = mid + 1
        return left