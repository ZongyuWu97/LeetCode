class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = collections.defaultdict(set)
        memo = set()
        for u, v in connections:
            memo.add((u, v))
            edges[u].add(v)
            edges[v].add(u)
        
        visited = set([0])
        stack = [0]
        cnt = 0
        while stack:
            node = stack.pop()
            for neighbor in edges[node]:
                if neighbor in visited:
                    continue
                visited.add(neighbor)
                if not (neighbor, node) in memo:
                    cnt += 1
                stack.append(neighbor)
        return cnt