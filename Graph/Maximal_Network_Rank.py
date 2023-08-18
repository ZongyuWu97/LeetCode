class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = collections.defaultdict(set)
        for u, v in roads:
            graph[u].add(v)
            graph[v].add(u)

        count = {}
        for i in range(n - 1):
            for j in range(i + 1, n):
                count[(i, j)] = len(graph[i]) + len(graph[j])
                if i in graph[j]:
                    count[(i, j)] -= 1
        return max(count.values())
