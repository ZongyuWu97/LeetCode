class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        self.memo = {}
        self.dfs1(0, -1, graph, price)
        self.max_diff = 0
        self.dfs2(0, -1, graph, price, 0)
        return self.max_diff

    def dfs1(self, root, parent, graph, price):
        m = 0
        for nei in graph[root]:
            if nei == parent:
                continue
            m = max(m, self.dfs1(nei, root, graph, price))
        self.memo[root] = m + price[root]
        return self.memo[root]

    def dfs2(self, root, parent, graph, price, parent_contribution):
        m1 = m2 = 0
        c1 = -1
        for nei in graph[root]:
            if nei == parent:
                continue
            if self.memo[nei] > m1:
                m2 = m1
                m1 = self.memo[nei]
                c1 = nei
            elif self.memo[nei] > m2:
                m2 = self.memo[nei]

        path1 = m1
        path2 = parent_contribution
        self.max_diff = max(path1, path2, self.max_diff)

        for nei in graph[root]:
            if nei == parent:
                continue
            if nei == c1:
                self.dfs2(nei, root, graph, price,
                          price[root] + max(parent_contribution, m2))
            else:
                self.dfs2(nei, root, graph, price,
                          price[root] + max(parent_contribution, m1))
