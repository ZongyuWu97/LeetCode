import heapq

class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        specialRoads = [(a, b, c, d, cost) for a, b, c, d, cost in specialRoads 
            if cost < abs(a - c) + abs(b - d)]
        distances = collections.defaultdict(lambda : float('inf'))
        distances[(start[0], start[1])] = 0
        h = [(0, start[0], start[1])]

        while h:
            distance, x, y = heapq.heappop(h)
            for a, b, c, d, cost in specialRoads:
                new_distance = distance + abs(x - a) + abs(y - b) + cost
                if new_distance < distances[(c, d)]:
                    distances[(c, d)] = new_distance
                    heapq.heappush(h, (new_distance, c, d))
        
        res = abs(target[0] - start[0]) + abs(target[1] - start[1])
        for c, d in distances:
            res = min(res, distances[(c, d)] + abs(target[0] - c) + abs(target[1] - d))
        return res
