import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        edges = []
        for idx, b in enumerate(buildings):
            edges.append((b[0], idx))
            edges.append((b[1], idx))
        edges.sort()

        res = []
        live = []
        i = 0
        n = len(edges)
        while i < n:
            curr_x = edges[i][0]

            while i < n and edges[i][0] == curr_x:
                b = buildings[edges[i][1]]
                if b[0] == curr_x:
                    heapq.heappush(live, (-b[2], b[1]))
                i += 1

            while live and live[0][1] <= curr_x:
                heapq.heappop(live)

            curr_height = -live[0][0] if live else 0
            if not res or res[-1][1] != curr_height:
                res.append((curr_x, curr_height))
        return res
