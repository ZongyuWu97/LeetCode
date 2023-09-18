from collections import deque
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0
            
        stops = collections.defaultdict(list)
        q = deque()
        end = set()
        visited = set()
        for i, route in enumerate(routes):
            for stop in route:
                stops[stop].append(i)
                if stop == source:
                    q.append((i, 1))
                    visited.add(i)
                if stop == target:
                    end.add(i)
        
        edges = collections.defaultdict(set)
        for stop in stops:
            buses = stops[stop]
            m = len(stops[stop])
            for u in range(m - 1):
                for v in range(u, m):
                    edges[buses[u]].add(buses[v])
                    edges[buses[v]].add(buses[u])
        
        while q:
            curr, dis = q.popleft()
            if curr in end:
                return dis
            for neighbor in edges[curr]:
                if not neighbor in visited:
                    visited.add(neighbor)
                    q.append((neighbor, dis + 1))
        return -1
        
