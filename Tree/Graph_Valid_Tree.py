from collections import defaultdict


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        self.count = 0

        def dfs(node):
            if node in seen:
                return
            seen.add(node)
            self.count += 1
            for neighbor in graph[node]:
                dfs(neighbor)

        dfs(0)
        return self.count == n and len(edges) == n - 1
